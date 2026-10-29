import json, re, hashlib, html
from pathlib import Path
import fitz

root = Path(__file__).resolve().parents[1]
acq = root / 'acquisition'
p = acq / 'acquisition-results.json'
rows = json.loads(p.read_text('utf-8'))
old = next(r for r in rows if r['id'] == 'E02')
assert old['doi'] == '10.1016/j.advwatres.2011.01.004'
pdf = root / 'papers/extraction/E02.pdf'
with fitz.open(pdf) as doc:
    first = doc[0].get_text()
    assert '10.1002/2017WR021480' in first
    counts = [len(page.get_text().strip()) for page in doc]
    abstract = first.split('Abstract', 1)[1].split('1. Introduction', 1)[0].strip()
new = dict(id='E02', split='extraction', doi='10.1002/2017wr021480',
    title='Real-Time Optimal Flood Control Decision Making and Risk Propagation Under Multiple Uncertainties',
    journal='Water Resources Research', year=2017, publication_date_parts=[2017,12,4],
    authors='Feilin Zhu; Ping-An Zhong; Yimeng Sun; William W.-G. Yeh',
    topic='risk_analysis', metadata_source='publisher_page_and_downloaded_pdf', metadata_verified=True,
    publisher_url='https://doi.org/10.1002/2017WR021480', abstract=abstract,
    local_source=None, prior_exposure='replacement_screened_by_title_and_abstract; no_pattern_extraction_in_current_run',
    eligibility='title_abstract_topic_screen_passed; fulltext_methods_quality_not_assessed',
    retrieved_date='2026-09-15', imported_date='2026-09-15', status='pdf_verified',
    file='papers\\extraction\\E02.pdf', access_kind='user_download_import',
    acquired_from='D:\\Downloads\\Water Resources Research - 2017 - Zhu - Real‐Time Optimal Flood Control Decision Making and Risk Propagation Under Multiple.pdf',
    version='user_downloaded_publisher_pdf_identity_checked', license='user_supplied_access; redistribution_not_assessed',
    selection_reason='多重不确定性下的实时防洪调度、预报—优化—决策及风险传播；替换主题关联不足的原 E02。',
    pdf_check=dict(pages=len(counts), doi_found_first_two_pages=True,
        sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(), text_characters_all_pages=sum(counts),
        pages_with_extractable_text=sum(c>50 for c in counts)))
archive = root / 'papers/background/Zhao_2011_forecast_uncertainty_former_E02.pdf'
assert hashlib.sha256(archive.read_bytes()).hexdigest() == old['pdf_check']['sha256']
(acq/'e02-replacement-record-20260915.json').write_text(json.dumps(dict(
    date='2026-09-15', authorization='User requested replacement of E02', old_record=old,
    archived_file=str(archive.relative_to(root)), new_record=new,
    reason='Original title/abstract does not explicitly establish a flood-control task; replacement explicitly studies real-time flood control.'), ensure_ascii=False,indent=2),'utf-8')
rows[rows.index(old)] = new
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
s = acq/'selection.json'
selection=json.loads(s.read_text('utf-8'))
selection=[new if r['id']=='E02' else r for r in selection]
s.write_text(json.dumps(selection,ensure_ascii=False,indent=2),'utf-8')
m=acq/'corpus-55.md'
t=m.read_text('utf-8')
line=f"| E02 | 2017 | {new['title']} | {new['journal']} | [{new['doi']}]({new['publisher_url']}) | [PDF](../papers/extraction/E02.pdf) | {new['selection_reason']} |"
t,n=re.subn(r'^\| E02 \|.*$',lambda _:line,t,flags=re.M);assert n==1
m.write_text(t,'utf-8')
r=acq/'corpus-55.ris'
blocks=r.read_text('utf-8').split('TY  - JOUR')
replacement='\n'+'\n'.join(['ID  - E02','TI  - '+new['title'],'JO  - '+new['journal'],'PY  - 2017','DO  - '+new['doi'],'UR  - '+new['publisher_url']]+['AU  - '+a for a in new['authors'].split('; ')]+['ER  - ','',''])
assert sum('ID  - E02\n' in b for b in blocks)==1
r.write_text('TY  - JOUR'.join(replacement if 'ID  - E02\n' in b else b for b in blocks),'utf-8')
h=acq/'download-checklist.html';t=h.read_text('utf-8')
pattern=r'<tr><td><code>E02.pdf</code>.*?</tr>'
def update_html(match):
    t=match.group().replace(old['title'],html.escape(new['title'])).replace(old['journal'],new['journal']).replace(old['publisher_url'],new['publisher_url']).replace('<td>2011</td>','<td>2017</td>')
    return t
t,n=re.subn(pattern,update_html,t);assert n==1;h.write_text(t,'utf-8')
e=acq/'topic-screening-excerpts.json';ex=json.loads(e.read_text('utf-8'))
ex=[dict(id='E02',title=new['title'],excerpt=abstract,pages=len(counts)) if x['id']=='E02' else x for x in ex]
e.write_text(json.dumps(ex,ensure_ascii=False,indent=2),'utf-8')
with (root/'run-notes.md').open('a',encoding='utf-8') as f:
    f.write('\n\n## 2026-09-15 E02 替换\n\n按用户指示，以 Zhu et al. (2017), DOI 10.1002/2017WR021480 替换原 E02。新 PDF 标题、DOI、20 页及可读性已核对；主题判断限于题目和摘要。原 Zhao et al. (2011) PDF 移至 papers/background/Zhao_2011_forecast_uncertainty_former_E02.pdf，不再计入 50 篇提取集。清单、RIS、HTML、selection 和主题摘录已同步；历史导入记录保留原样，变更见 acquisition/e02-replacement-record-20260915.json。正式集仍为 50 篇提取 + 5 篇 validation，背景文献 2 篇。\n')
assert len(rows)==55 and len({r['doi'].lower() for r in rows})==55
assert len(list((root/'papers/extraction').glob('*.pdf')))==50
assert len(list((root/'papers/validation').glob('*.pdf')))==5
assert all((root/r['file']).exists() for r in rows)
print('Verified: E02 replaced; 50 extraction + 5 validation; old E02 archived; catalogs updated.')
