import json,csv,re,html,collections
from pathlib import Path
import fitz
from acquire import ROOT,PROJECT,pdf_check

p=ROOT/'acquisition/acquisition-results.json'
rows=json.loads(p.read_text('utf-8'))
assert len(rows)==55 and len({x['doi'] for x in rows})==55
old=list(csv.DictReader((PROJECT/'artifacts/run-20260902-flood-risk-expanded-skill-study/data/rapid-topic-paper-set.csv').open(encoding='utf-8-sig')))
oldmap={x['doi_or_url'].lower():x for x in old}
public_sources={'E13':'https://repository.library.noaa.gov/view/noaa/64804/noaa_64804_DS1.pdf','E50':'https://par.nsf.gov/servlets/purl/10530470'}
fixes=[]
for r in rows:
 r['selection_reason']={
 'prior_0902':'0902 主题候选重新核验；直接涉及防洪规则、预报风险、FIRO 或运行实施。',
 'risk_calibration':'对防洪模型参数进行风险校准，连接决策权衡与验证。',
 'event_operation':'真实洪水事件中的多库联合决策与制度协调。',
 'ensemble_operation':'集合预报不确定性与防洪调度连接。',
 'hedging':'预泄/洪水资源利用中当前与未来风险的分配。',
 'forecast_error':'预报误差及其对防洪运行风险的影响。',
 'dynamic_level':'不确定性下的汛限水位动态调整。',
 'risk_analysis':'防洪运行风险量化与决策支持。',
 'multi_reservoir_risk':'多库运行中的风险传播、诊断或协调。',
 'multi_reservoir_stochastic':'不确定预报下的多阶段、多库防洪与蓄水决策。',
 'tree_mpc':'情景树与滚动优化处理预报不确定性。',
 'scenario_tree':'情景树表示不确定性及防洪风险验证。',
 'forecast_operation':'基于预报的运行规则与常规规则比较。',
 'risk_preferences':'多库防洪风险指标、偏好与方案选择。',
 'ensemble_risk':'集合预报下的两阶段防洪风险分析。',
 'compound_risk':'防洪与发电风险权衡；防洪为实质评价项。',
 'multi_reservoir_mpc':'多库防洪规则改进与滚动控制。',
 'multi_reservoir_dynamic_level':'河道传播与多库动态水位边界。',
 'adaptive_level':'非平稳来水风险下的自适应汛限水位。',
 'staged_rules':'分阶段防洪运行规则。',
 'decision_criteria':'防洪方案的指标选择、相关性与决策权衡。',
 'robust_risk_decision':'预报不确定性下的稳健防洪与风险决策。',
 'forecast_policy_variation':'多水库 FIRO 策略差异与适用条件。',
 'operator_risk_mpc':'操作人员偏好与实时防洪控制（验证候选）。',
 'robust_optimization':'稳健防洪优化（验证候选）。',
 'multi_reservoir_uncertainty':'概率预报与多库随机防洪决策（验证候选）。',
 'adaptive_rules':'洪水形状不确定性与自适应运行规则（验证候选）。',
 }[r['topic']]
 r['prior_exposure']='0902_candidate_or_audited_anchor' if r['doi'] in oldmap or r['id'] in ['E20','E21','E22','E23'] else 'not_used_for_skill_extraction_in_current_run'
 if r['split']=='validation':
  r['prior_exposure']='metadata_seen_in_prior_search_queue_only; not_assessed_or_acquired_in_prior_ledger' if r['id']=='V03' else 'no_doi_hit_in_prior_project_artifact_search'
  r['holdout_status']='reserved; acquisition_metadata_and_file_identity_only; no_pattern_extraction_or_skill_revision'
 if r['doi'] in oldmap:
  o=oldmap[r['doi']]
  if o['title']!=r['title'] or str(o['year'])!=str(r['year']):fixes.append((r['id'],o['title'],r['title'],o['year'],r['year']))
 if r['status']=='pdf_verified':
  check=pdf_check(ROOT/r['file'],r['title'],r['doi']); assert check
  with fitz.open(ROOT/r['file']) as d:
   counts=[len(page.get_text().strip()) for page in d]
   check['text_characters_all_pages']=sum(counts)
   check['pages_with_extractable_text']=sum(c>50 for c in counts)
  r['pdf_check']=check
  if r.get('access_kind')=='user_download_import':
   pass  # Preserve the original user-download path and import provenance.
  elif r.get('local_source'):
   r.update(acquired_from=str(PROJECT/'data/paper'/r['local_source']),access_kind='user_supplied_existing',version='existing_local_copy',license='not_reassessed_user_supplied')
  elif r['id'] in public_sources:r.update(acquired_from=public_sources[r['id']],access_kind='public_repository',version='repository_copy',license='see_article')
  else:
   doi=r['doi']; m=re.fullmatch('10.3390/([a-z]+)([0-9]+)',doi)
   assert m
   journal={'w':'water','hydrology':'hydrology'}[m[1]]; digits=m[2]; base=f'{journal}-{int(digits[:2]):02d}-{int(digits[4:]):05d}'
   r.update(acquired_from=f'https://mdpi-res.com/d_attachment/{journal}/{base}/article_deploy/{base}.pdf',access_kind='public_download',version='publisher_pdf',license='see_article')
 else:
  r['download_reason']='有公开全文线索，但自动下载被站点拒绝或未取得有效 PDF' if r.get('oa_status') not in ['closed','unknown',None] else '未取得公开 PDF；请先尝试机构访问（不代表已证明没有公开版本）'
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
got=[r for r in rows if r['status']=='pdf_verified'];missing=[r for r in rows if r['status']!='pdf_verified']
assert len(got)==len(list((ROOT/'papers/extraction').glob('*.pdf')))+len(list((ROOT/'papers/validation').glob('*.pdf')))

intro=f'''# 55 篇文献获取清单

更新日期：2026-09-15

| 用途 | 计划清单 | 已取得并检查的 PDF | 待补全文 |
|---|---:|---:|---:|
| Pattern 提取 E01–E50 | 50 | {sum(r['split']=='extraction' for r in got)} | {sum(r['split']=='extraction' for r in missing)} |
| Validation 预留 V01–V05 | 5 | {sum(r['split']=='validation' for r in got)} | {sum(r['split']=='validation' for r in missing)} |
| 合计 | 55 | {len(got)} | {len(missing)} |

55 篇是已核验 DOI/正式标题的下载候选，不等于 55 篇全文已获取或正式纳入。全文方法适用性和证据质量仍需后续审核；不合格项将以同类候选替换并记录理由。已取得 PDF 检查了可读性、首页 DOI/标题匹配、页数及文本可提取性，不代表已完成内容审计。

## 下载方式

1. 优先按下方“需要你下载”的表格打开 DOI，使用学校/机构权限下载文章正文 PDF；不是摘要页或补充材料。
2. 推荐按编号命名，例如 `E01.pdf`、`V01.pdf`，放入 [papers/user-downloads/](../papers/user-downloads/)。保留原文件名也可以，后续可按 DOI 匹配。
3. 已有 PDF 无需重复下载。[全部 55 篇目录](corpus-55.md)列出已获取文件和题录。
4. 验证集暂不用于 pattern 提取或技能修改。V03 曾出现在旧检索队列，但旧账本标明未获取、未评估；这里只做预留，不宣称模型训练语料层面的完全未见。

## 需要你下载

“公开版本下载失败”与“需要订阅”不是一回事；前者可能在普通浏览器中即可下载。
'''
def md_table(rs):
 out=['| 编号／建议文件名 | 年份 | 正式标题 | 期刊 | 下载入口 | 状态 |','|---|---:|---|---|---|---|']
 for r in rs:
  out.append(f"| `{r['id']}.pdf` | {r['year']} | {r['title']} | {r['journal']} | [DOI]({r['publisher_url']}) | {r.get('download_reason','已获取')} |")
 return '\n'.join(out)
priority=[r for r in missing if r['doi'] in oldmap or r['id'] in ['E20','E21','E22','E23']]
new=[r for r in missing if r not in priority and r['split']=='extraction']
val=[r for r in missing if r['split']=='validation']
doc=intro+'\n### 1. 0902 相关核心文献优先补齐\n\n'+md_table(priority)+'\n\n### 2. 新增提取文献\n\n'+md_table(new)+'\n\n### 3. 独立 validation 预留文献\n\n'+md_table(val)+'\n'
(ROOT/'acquisition/download-needed.md').write_text(doc,'utf-8')
cat=['# 全部 55 篇下载候选与文件状态','','日期：2026-09-15；年份默认 Crossref 首次出版年，可能与卷期年份不同。正式引用时保留两类日期。','','| ID | 年份 | 标题 | 期刊 | DOI | 文件 | 纳入候选理由 |','|---|---:|---|---|---|---|---|']
for r in rows:
 file='[PDF](../'+r['file'].replace('\\','/')+')' if r['file'] else '待补全文'
 cat.append(f"| {r['id']} | {r['year']} | {r['title']} | {r['journal']} | [{r['doi']}]({r['publisher_url']}) | {file} | {r['selection_reason']} |")
(ROOT/'acquisition/corpus-55.md').write_text('\n'.join(cat)+'\n','utf-8')
ris=[]
for r in rows:
 ris += ['TY  - JOUR','ID  - '+r['id'],'TI  - '+r['title'],'JO  - '+r['journal'],'PY  - '+str(r['year']),'DO  - '+r['doi'],'UR  - '+r['publisher_url']]+['AU  - '+a for a in r['authors'].split('; ') if a]+['ER  - ','']
(ROOT/'acquisition/corpus-55.ris').write_text('\n'.join(ris),'utf-8')
cor=['# 旧候选表书目信息校正','','以 DOI 注册元数据校正；不改旧文件。年份采用首次出版年，卷期年可能不同。','','| ID | 旧标题 | 核验标题 | 旧年 | 注册出版年 |','|---|---|---|---:|---:|']
cor += [f'| {i} | {o} | {n} | {oy} | {ny} |' for i,o,n,oy,ny in fixes]
(ROOT/'acquisition/bibliographic-corrections.md').write_text('\n'.join(cor)+'\n','utf-8')
# Read-only browser-friendly handoff; no external scripts or dependencies.
def table(rs):
 h='<table><thead><tr><th>编号</th><th>年份</th><th>标题 / 期刊</th><th>下载 / 文件</th><th>说明</th></tr></thead><tbody>'
 for r in rs:
  link=f'<a href="{html.escape(r["publisher_url"])}" target="_blank">出版社 / DOI</a>'
  if r['file']:link+=f'<br><a href="../{r["file"].replace(chr(92),"/")}">已获取 PDF</a>'
  h+=f'<tr><td><code>{r["id"]}.pdf</code></td><td>{r["year"]}</td><td>{html.escape(r["title"])}<small>{html.escape(r["journal"])}</small></td><td>{link}</td><td>{html.escape(r.get("download_reason","已获取并核对文件"))}</td></tr>'
 return h+'</tbody></table>'
page=f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>55 篇文献下载清单</title><style>body{{font:16px/1.6 system-ui,sans-serif;max-width:1400px;margin:36px auto;padding:0 24px;color:#193047;background:#f7f9fb}}h1,h2{{color:#143e59}}table{{border-collapse:collapse;width:100%;background:white;margin:20px 0 36px}}td,th{{text-align:left;padding:12px;border-bottom:1px solid #dce3e8;vertical-align:top}}th{{background:#e9eff4}}small{{display:block;color:#667}}a{{color:#075b9a}}code{{white-space:nowrap}}.summary{{padding:18px;background:#e4f0ec;border-radius:8px}}</style><h1>55 篇文献下载清单</h1><p>2026-09-15 · 洪水主题 · 50 篇提取 + 5 篇验证预留</p><div class="summary">已取得并核对 <b>{len(got)}</b> 篇 PDF；还需补 <b>{len(missing)}</b> 篇。55 篇为下载候选，全文纳入审核尚未完成。</div><p>点击 DOI 使用学校/机构权限下载正文，按编号命名，例如 E01.pdf，放入 <a href="../papers/user-downloads/">papers/user-downloads/</a>。公开版本自动下载失败的条目，可能可以直接在普通浏览器下载。</p><h2>优先补齐：0902 核心文献（{len(priority)} 篇）</h2>{table(priority)}<h2>新增提取文献（{len(new)} 篇）</h2>{table(new)}<h2>验证预留（{len(val)} 篇待补）</h2>{table(val)}<h2>已经取得（{len(got)} 篇）</h2>{table(got)}<p>验证论文仅做获取和身份核对，不进入 pattern 开发。V03 在旧队列出现过题录，未获取/评估。PDF 校验不等于全文证据审计。</p></html>'''
(ROOT/'acquisition/download-checklist.html').write_text(page,'utf-8')
print(json.dumps({'selected':len(rows),'pdf_verified':len(got),'missing':len(missing),'priority_missing':len(priority),'new_extraction_missing':len(new),'validation_missing':len(val),'bibliographic_corrections':len(fixes)},ensure_ascii=False))
