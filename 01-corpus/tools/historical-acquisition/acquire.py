import csv, json, re, time, shutil, hashlib, html, concurrent.futures as cf
from pathlib import Path
import requests, fitz
from collect import ROOT, PROJECT, CACHE, get_doi

EXTRA=[
('10.5194/nhess-13-965-2013','risk_calibration'),
('10.1038/s41598-022-06801-8','event_operation'),
('10.1007/s11269-024-04089-z','ensemble_operation'),
('10.1007/s11269-014-0899-1','ensemble_operation'),
('10.1061/(ASCE)WR.1943-5452.0000432','hedging'),
('10.1007/s11269-016-1472-x','hedging'),
('10.1007/s11269-020-02571-y','hedging'),
('10.1007/s11269-015-1080-1','forecast_error'),
('10.1007/s00477-013-0756-4','forecast_error'),
('10.1061/(ASCE)HE.1943-5584.0000979','dynamic_level'),
('10.1061/(ASCE)WR.1943-5452.0000490','risk_analysis'),
('10.1061/(ASCE)WR.1943-5452.0001174','risk_analysis'),
('10.1016/j.envsoft.2018.10.007','multi_reservoir_risk'),
('10.1016/j.jhydrol.2019.123954','multi_reservoir_risk'),
('10.1016/j.jhydrol.2020.125513','multi_reservoir_stochastic'),
('10.3390/w10030340','tree_mpc'),
('10.3390/w10050606','scenario_tree'),
('10.3390/w11061134','forecast_operation'),
('10.3390/w11040649','risk_preferences'),
('10.1007/s11269-021-02795-6','risk_analysis'),
('10.1007/s00477-014-0986-0','ensemble_risk'),
('10.1016/j.jhydrol.2015.09.012','dynamic_level'),
('10.3390/w13020173','compound_risk'),
('10.3390/w10101371','multi_reservoir_mpc'),
('10.1111/jfr3.12586','multi_reservoir_dynamic_level'),
('10.1061/(ASCE)WR.1943-5452.0000906','adaptive_level'),
('10.1016/j.jhydrol.2014.11.073','staged_rules'),
('10.2166/hydro.2017.059','decision_criteria'),
('10.2166/hydro.2015.055','decision_criteria'),
('10.1016/j.jhydrol.2021.127334','robust_risk_decision'),
('10.1061/JWRMD5.WRENG-6471','forecast_policy_variation'),
]
VALIDATION=[
('10.1007/s11269-025-04305-4','dynamic_level'),
('10.2166/hydro.2025.019','operator_risk_mpc'),
('10.1016/j.jhydrol.2023.129421','robust_optimization'),
('10.1016/j.jhydrol.2025.134285','multi_reservoir_uncertainty'),
('10.3390/hydrology11090147','adaptive_rules'),
]

def clean(s): return html.unescape(re.sub('<[^>]*>','',s)).strip()
def norm(s): return re.sub('[^a-z0-9]','',s.lower())
def api_openalex(doi):
 p=CACHE/('oa-'+re.sub('[^a-z0-9]+','-',doi.lower())+'.json')
 if p.exists(): return json.loads(p.read_text('utf-8'))
 for i in range(3):
  try:
   r=requests.get('https://api.openalex.org/works/https://doi.org/'+doi,timeout=30)
   if r.status_code==429: time.sleep(2+i); continue
   r.raise_for_status(); x=r.json(); p.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf-8'); return x
  except Exception: time.sleep(.5)
 return {}

def pdf_check(p,title,doi):
 try:
  with fitz.open(p) as doc:
   if len(doc)<3: return None
   txt=' '.join(doc[i].get_text() for i in range(min(2,len(doc))))
   words=set(re.findall('[a-z]{4,}',title.lower()))-{'with','from','using','based','under','during','considering','operation','reservoir','control','flood'}
   overlap=sum(w in txt.lower() for w in words)/max(len(words),1)
   doi_match=norm(doi) in norm(txt)
   # Exact title anywhere in first two pages or most distinctive title tokens.
   if not doi_match and norm(title) not in norm(txt) and overlap<.85: return None
   if len(txt)<500:return None
   return {'pages':len(doc),'doi_found_first_two_pages':doi_match,'title_token_overlap':round(overlap,3),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 except Exception:return None

def download_one(row):
 doi=row['doi']; title=row['title']; destination=ROOT/'papers'/row['split']/(row['id']+'.pdf')
 log=[]
 if destination.exists():
  check=pdf_check(destination,title,doi)
  if check: row.update(status='pdf_verified',file=str(destination.relative_to(ROOT)),pdf_check=check); return row
 local=row.get('local_source')
 if local:
  p=PROJECT/'data/paper'/local
  check=pdf_check(p,title,doi)
  if check:
   shutil.copy2(p,destination); row.update(status='pdf_verified',file=str(destination.relative_to(ROOT)),pdf_check=check,acquired_from=str(p),access_kind='user_supplied_existing'); return row
 oa=api_openalex(doi)
 row['openalex_id']=oa.get('id',''); row['oa_status']=oa.get('open_access',{}).get('oa_status','unknown')
 urls=[]
 for l in oa.get('locations',[]):
  if l.get('pdf_url'): urls.append((l['pdf_url'],l.get('license'),l.get('version')))
 # publisher-hosted direct PDF for MDPI; no authentication bypass.
 if doi.startswith('10.3390/'):
  m=re.fullmatch('10.3390/([a-z]+)([0-9]+)',doi)
  if m:
   journal={'w':'water','hydrology':'hydrology'}.get(m[1]); digits=m[2]
   if journal:
    vol=int(digits[:2]); article=int(digits[4:]); base=f'{journal}-{vol:02d}-{article:05d}'
    urls.insert(0,(f'https://mdpi-res.com/d_attachment/{journal}/{base}/article_deploy/{base}.pdf',None,'publishedVersion'))
 for link in row.get('crossref_links',[]):
  u=link.get('URL','')
  if 'pdf' in link.get('content-type','') or '.pdf' in u:urls.append((u,None,'publisher_link'))
 if doi.startswith('10.1007/'): urls.append(('https://link.springer.com/content/pdf/'+doi+'.pdf',None,'publishedVersion'))
 if doi.startswith('10.1029/') or doi.startswith('10.1002/') or doi.startswith('10.1111/'):
  host='agupubs.onlinelibrary.wiley.com' if doi.startswith('10.1029/') or 'wr0' in doi else 'onlinelibrary.wiley.com'
  urls.append(('https://'+host+'/doi/pdfdirect/'+doi,None,'publishedVersion'))
 seen=set()
 for url,license,version in urls[:7]:
  if url in seen:continue
  seen.add(url)
  try:
   r=requests.get(url,timeout=(10,25),headers={'User-Agent':'Mozilla/5.0 (academic literature retrieval)'})
   if r.status_code==200 and r.content.startswith(b'%PDF'):
    temp=ROOT/'acquisition'/(row['id']+'-download.tmp')
    temp.write_bytes(r.content); check=pdf_check(temp,title,doi)
    if check:
     temp.replace(destination); row.update(status='pdf_verified',file=str(destination.relative_to(ROOT)),pdf_check=check,acquired_from=r.url,access_kind='public_download',license=license or 'not_recorded',version=version,attempts=log); return row
    temp.unlink(); log.append({'url':url,'result':'pdf_identity_or_completeness_check_failed'})
   else:log.append({'url':url,'result':str(r.status_code),'content_type':r.headers.get('Content-Type','')})
  except Exception as e:log.append({'url':url,'result':type(e).__name__})
 row.update(status='user_download_needed',file='',attempts=log)
 return row

def main():
 old=list(csv.DictReader((PROJECT/'artifacts/run-20260902-flood-risk-expanded-skill-study/data/rapid-topic-paper-set.csv').open(encoding='utf-8-sig')))
 local=list(csv.DictReader((PROJECT/'data/paper/manifest.csv').open(encoding='utf-8-sig')))
 localmap={x['doi'].lower():x['file'] for x in local}
 localmap['10.3390/w12030892']='water-12-00892.pdf'
 localmap['10.1016/j.jhydrol.2022.128665']='1-s2.0-S0022169422012355-main.pdf'
 # Verify old anchor DOI from local manifest instead of relying on a remembered identifier.
 for x in local:
  if x['title'].lower().startswith('risk-based methodology for parameter calibration'):
   EXTRA[0]=(x['doi'].lower(),'risk_calibration')
 candidates={x['DOI'].lower():x for x in json.loads((ROOT/'acquisition/candidates.json').read_text('utf-8'))}
 selection=[(x['doi_or_url'].lower(),'prior_0902','extraction') for x in old if x['paper_id']!='P18']
 selection += [(d.lower(),g,'extraction') for d,g in EXTRA]
 selection += [(d.lower(),g,'validation') for d,g in VALIDATION]
 assert len(selection)==55 and len({d for d,_,_ in selection})==55
 rows=[];counts={'extraction':0,'validation':0}
 for d,g,split in selection:
  x=candidates.get(d,{})
  if not x:
   for attempt in range(3):
    x=get_doi(d)
    if 'error' not in x:break
    time.sleep(1+attempt)
  oa={}
  if not x.get('title'):oa=api_openalex(d)
  title=clean(' '.join(x.get('title',[])) or oa.get('title',''))
  counts[split]+=1; pid=('E' if split=='extraction' else 'V')+f'{counts[split]:02d}'
  if not title: raise RuntimeError('No verified title: '+d)
  journal=clean(' '.join(x.get('container-title',[]))) or ((oa.get('primary_location') or {}).get('source') or {}).get('display_name','')
  date=x.get('published',{}).get('date-parts',[[oa.get('publication_year','')]])[0]
  rows.append({'id':pid,'split':split,'doi':d,'title':title,'journal':journal,'publication_date_parts':date,'year':date[0],'authors':'; '.join((a.get('given','')+' '+a.get('family','')).strip() for a in x.get('author',[])),'topic':g,'metadata_source':'Crossref' if x.get('title') else 'OpenAlex','metadata_verified':True,'publisher_url':'https://doi.org/'+d,'crossref_links':x.get('link',[]),'abstract':clean(x.get('abstract','')),'local_source':localmap.get(d),'prior_exposure':'previous_candidate_or_local_collection' if d in localmap or any(z['doi_or_url'].lower()==d for z in old) else 'not_in_0902_or_local_manifest; other_prior_runs_not_exhaustively_checked','eligibility':'title_abstract_candidate; fulltext_eligibility_pending','retrieved_date':'2026-09-15'})
 (ROOT/'acquisition/selection.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
 print('VERIFIED_METADATA',len(rows),flush=True)
 results=[]
 with cf.ThreadPoolExecutor(max_workers=3) as ex:
  futures={ex.submit(download_one,r):r['id'] for r in rows}
  for f in cf.as_completed(futures):
   try:r=f.result(); results.append(r); print(r['id'],r['status'],flush=True)
   except Exception as e:print('ERROR',futures[f],repr(e),flush=True)
   (ROOT/'acquisition/acquisition-results.json').write_text(json.dumps(sorted(results,key=lambda x:x['id']),ensure_ascii=False,indent=2),'utf-8')
 print('DONE',len(results),'DOWNLOADED',sum(r['status']=='pdf_verified' for r in results),flush=True)

if __name__=='__main__':main()
