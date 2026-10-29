import json, requests
from acquire import ROOT,pdf_check

URLS={
 'E13':'https://repository.library.noaa.gov/view/noaa/64804/noaa_64804_DS1.pdf',
 'E50':'https://par.nsf.gov/servlets/purl/10530470',
 'V02':'https://research.tudelft.nl/files/241329954/jh2025019-1.pdf',
}
path=ROOT/'acquisition/acquisition-results.json'
rows=json.loads(path.read_text('utf-8'))
for row in rows:
 if row['id'] not in URLS:continue
 u=URLS[row['id']]
 try:
  r=requests.get(u,timeout=35)
  if r.status_code!=200 or not r.content.startswith(b'%PDF'):
   print(row['id'],r.status_code,'not_pdf',flush=True);continue
  tmp=ROOT/'acquisition'/(row['id']+'-repository.tmp');tmp.write_bytes(r.content)
  check=pdf_check(tmp,row['title'],row['doi'])
  if not check:tmp.unlink(); print(row['id'],'identity_failed',flush=True);continue
  dest=ROOT/'papers'/row['split']/(row['id']+'.pdf');tmp.replace(dest)
  row.update(status='pdf_verified',file=str(dest.relative_to(ROOT)),pdf_check=check,acquired_from=r.url,access_kind='public_repository',version='repository_copy_identity_checked',license='see_article')
  print(row['id'],'pdf_verified',flush=True)
 except Exception as e:print(row['id'],type(e).__name__,flush=True)
path.write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
