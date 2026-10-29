"""Inspect user downloads and prepare an explicit, non-overwriting move plan."""
import json,re,hashlib,sys
from datetime import datetime
from pathlib import Path
import fitz
from acquire import ROOT,pdf_check,norm

SOURCE=Path('C:/Users/zihanz10/Downloads').resolve()
RESULTS=ROOT/'acquisition/acquisition-results.json'
PLAN=ROOT/'acquisition/user-import-plan-20260915.json'

def inspect():
 rows=json.loads(RESULTS.read_text('utf-8'))
 files=[p for p in SOURCE.glob('*.pdf') if datetime.fromtimestamp(p.stat().st_mtime).date().isoformat()=='2026-09-15']
 moves=[];issues=[]
 for p in files:
  try:
   with fitz.open(p) as doc:
    text=' '.join(doc[i].get_text() for i in range(min(2,len(doc))))
    nt=norm(text)
    matches=[r for r in rows if norm(r['doi']) in nt]
    if len(matches)>1:
     # A references section might introduce another DOI; require title evidence too.
     matches=[r for r in matches if norm(r['title']) in nt]
    if len(matches)!=1:
     issues.append({'source':str(p),'reason':'DOI_match_not_unique','matches':[r['id'] for r in matches]});continue
    r=matches[0]; check=pdf_check(p,r['title'],r['doi'])
    if not check:issues.append({'source':str(p),'reason':'identity_or_pdf_check_failed'});continue
    # Ensure the expected paper's title also matches, beyond a DOI mention.
    if check['title_token_overlap']<.75:
     issues.append({'source':str(p),'reason':'title_needs_manual_review','id':r['id'],'check':check});continue
    lengths=[len(page.get_text().strip()) for page in doc]
    check.update(text_characters_all_pages=sum(lengths),pages_with_extractable_text=sum(n>50 for n in lengths))
    dest=(ROOT/'papers'/r['split']/(r['id']+'.pdf')).resolve()
    if dest.exists():issues.append({'source':str(p),'reason':'destination_already_exists','id':r['id']});continue
    moves.append({'id':r['id'],'title':r['title'],'doi':r['doi'],'source':str(p.resolve()),'destination':str(dest),'sha256':check['sha256'],'pdf_check':check})
  except Exception as e:issues.append({'source':str(p),'reason':str(e)})
 if len({m['id'] for m in moves})!=len(moves):raise RuntimeError('Duplicate matches in source batch')
 pending=[r['id'] for r in rows if r['status']!='pdf_verified' and r['id'] not in {m['id'] for m in moves}]
 plan={'source_directory':str(SOURCE),'run_directory':str(ROOT.resolve()),'inspected_files':len(files),'moves':sorted(moves,key=lambda m:m['id']),'issues':issues,'remaining_missing_after_move':pending}
 PLAN.write_text(json.dumps(plan,ensure_ascii=False,indent=2),'utf-8')
 print(json.dumps({'inspected':len(files),'matched':len(moves),'issues':issues,'remaining':pending},ensure_ascii=False))
 for m in plan['moves']:print(m['id'],m['pdf_check']['pages'],'pages',m['source'].split('\\')[-1])

def finalize():
 plan=json.loads(PLAN.read_text('utf-8'));rows=json.loads(RESULTS.read_text('utf-8'));byid={r['id']:r for r in rows}
 for m in plan['moves']:
  dest=Path(m['destination']);assert dest.is_file() and not Path(m['source']).exists()
  assert hashlib.sha256(dest.read_bytes()).hexdigest()==m['sha256']
  r=byid[m['id']]
  r.update(status='pdf_verified',file=str(dest.relative_to(ROOT)),pdf_check=m['pdf_check'],acquired_from=m['source'],access_kind='user_download_import',version='user_downloaded_publisher_pdf_identity_checked',license='user_supplied_access; redistribution_not_assessed',imported_date='2026-09-15')
  r.pop('download_reason',None)
 RESULTS.write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
 report=['# 用户下载文件整理记录','','日期：2026-09-15','','按首页/前两页 DOI 与标题核对后移动；对全部页面做解析和文本可提取性检查。移动前后核对 SHA256，未覆盖任何已有文件。正文科学内容和出版版本完整性仍需后续审计。','','| 编号 | 原文件名 | 新位置 | 页数 |','|---|---|---|---:|']
 for m in plan['moves']:
  report.append(f"| {m['id']} | {Path(m['source']).name} | `{Path(m['destination']).relative_to(ROOT)}` | {m['pdf_check']['pages']} |")
 report+=['','## 问题与缺件','',json.dumps({'issues':plan['issues'],'remaining_missing':plan['remaining_missing_after_move']},ensure_ascii=False),'','验证集仅做文件身份与完整性初检，不开展 pattern 提取。']
 (ROOT/'acquisition/user-import-report-20260915.md').write_text('\n'.join(report),'utf-8')
 print('Imported',len(plan['moves']),'Verified corpus',sum(r['status']=='pdf_verified' for r in rows))

if __name__=='__main__':finalize() if '--finalize' in sys.argv else inspect()
