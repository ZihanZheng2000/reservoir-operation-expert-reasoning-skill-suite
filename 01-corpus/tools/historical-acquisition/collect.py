import csv, json, re, time, concurrent.futures as cf
from pathlib import Path
import requests

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parents[1]
CACHE=ROOT/'acquisition/metadata'
CACHE.mkdir(exist_ok=True)
S=requests.Session()
S.headers['User-Agent']='ReservoirLiteratureAcquisition/1.0 (academic metadata verification)'
QUERIES=[
 'reservoir flood control forecast uncertainty',
 'reservoir flood limited water level dynamic control risk',
 'forecast informed reservoir operations prerelease',
 'reservoir flood control robust stochastic optimization',
 'reservoir flood control ensemble model predictive control',
 'multi reservoir flood operation uncertainty risk',
 'reservoir flood hedging operating rules forecast',
]

def fetch_query(q):
 p=CACHE/('query-'+re.sub('[^a-z0-9]+','-',q.lower())+'.json')
 if p.exists(): return json.loads(p.read_text('utf-8'))
 r=S.get('https://api.crossref.org/works',params={'query':q,'rows':60,'filter':'type:journal-article,until-pub-date:2026-09-15'},timeout=50)
 r.raise_for_status(); data=r.json()['message']; p.write_text(json.dumps(data,ensure_ascii=False,indent=2),'utf-8')
 return data

def get_doi(doi):
 p=CACHE/('doi-'+re.sub('[^a-z0-9]+','-',doi.lower())+'.json')
 if p.exists(): return json.loads(p.read_text('utf-8'))
 try:
  r=S.get('https://api.crossref.org/works/'+requests.utils.quote(doi,safe=''),timeout=35)
  r.raise_for_status(); data=r.json()['message']; p.write_text(json.dumps(data,ensure_ascii=False,indent=2),'utf-8'); return data
 except Exception as e: return {'DOI':doi,'error':str(e)}

def main():
 records={}
 with cf.ThreadPoolExecutor(max_workers=1) as ex:
  futs={ex.submit(fetch_query,q):q for q in QUERIES}
  for f in cf.as_completed(futs):
   q=futs[f]
   try:
    data=f.result()
    for x in data['items']:
     d=x['DOI'].lower(); records.setdefault(d,x); records[d].setdefault('_queries',[]).append(q)
    print('QUERY',q,len(data['items']),flush=True)
   except Exception as e: print('ERROR',q,str(e),flush=True)
 old=list(csv.DictReader((PROJECT/'artifacts/run-20260902-flood-risk-expanded-skill-study/data/rapid-topic-paper-set.csv').open(encoding='utf-8-sig')))
 local=list(csv.DictReader((PROJECT/'data/paper/manifest.csv').open(encoding='utf-8-sig')))
 wanted={x['doi_or_url'].lower():x for x in old}
 local_rel={x['doi'].lower():x for x in local if re.search('flood|ensemble|inferred inflow',x['title'],re.I)}
 with cf.ThreadPoolExecutor(max_workers=1) as ex:
  for x in ex.map(get_doi,sorted(set(wanted)|set(local_rel))):
   d=x['DOI'].lower()
   if 'error' not in x: records.setdefault(d,x)
 for d,x in records.items():
  x['_prior_0902']=wanted.get(d)
  x['_local']=local_rel.get(d)
 out=ROOT/'acquisition/candidates.json'
 out.write_text(json.dumps(list(records.values()),ensure_ascii=False,indent=2),'utf-8')
 rows=[]
 for d,x in records.items():
  title=' '.join(x.get('title',[])); abstract=re.sub('<[^>]+>',' ',x.get('abstract',''))
  if ('reservoir' in title.lower() or 'dam' in title.lower()) and re.search('flood|forecast|pre.release',title,re.I):
   year=x.get('published',{}).get('date-parts',[[0]])[0][0]
   rows.append((year,d,title,' '.join(x.get('container-title',[])),bool(x['_prior_0902']),bool(x['_local'])))
 rows.sort(key=lambda r:(not r[4],-r[0],r[2]))
 (ROOT/'acquisition/candidate-screening.txt').write_text('\n'.join(f'{i+1:03d} | {y} | {d} | {t} | {j} | old={o} local={l}' for i,(y,d,t,j,o,l) in enumerate(rows)),'utf-8')
 print('TOTAL',len(records),'TITLE_SCREEN',len(rows),flush=True)

if __name__=='__main__': main()
