"""Freeze explicit public paths; excludes source books and private extraction."""
from pathlib import Path
import hashlib,json,zipfile,re
root=Path(__file__).resolve().parents[1]
paths=['.gitignore','.gitattributes','README.md','VERSION','CHANGELOG.md','RELEASE_NOTES.md','CONTRIBUTORS.md','THIRD_PARTY_NOTICES.md']
for directory in ['skills/mind_skill','docs','examples','evaluation','scripts','tests']:
 paths.extend(p.relative_to(root).as_posix() for p in (root/directory).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
paths=sorted(set(paths))
for p in paths:
 if not p.endswith('.zip'):
  target=root/p
  target.write_bytes(target.read_text(encoding='utf-8').encode('utf-8'))
release=root/'releases/v0.1.0';release.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(release/'mind_skill.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in paths:
  if p.startswith('skills/mind_skill/'):z.write(root/p,p.removeprefix('skills/'))
with zipfile.ZipFile(release/'mind_skill.zip') as z:assert z.testzip() is None
paths.append('releases/v0.1.0/mind_skill.zip')
records=[]
for p in paths:
 b=(root/p).read_bytes()
 if not p.endswith('.zip'):
  assert not re.search(rb'[A-Z]:[/\\]Users[/\\][A-Za-z0-9]',b),p
 records.append(dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob_sha1=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()))
pub=root/'publication';pub.mkdir(exist_ok=True)
(pub/'PUBLIC_MANIFEST.json').write_text(json.dumps({'version':'0.1.0','scope':'files listed only; excludes manifest, SHA256SUMS, add plan and local receipts to avoid recursion','files':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
(pub/'SHA256SUMS').write_text(''.join(x['sha256']+'  '+x['path']+'\n' for x in records),encoding='utf-8',newline='\n')
(pub/'change-plan.md').write_text('# 初始公开变更计划\n\n空仓库仅建立README的main基线；本次主题分支新增以下路径，无删除或重命名。\n\n'+''.join('- add `'+p+'`\n' for p in paths+['publication/PUBLIC_MANIFEST.json','publication/SHA256SUMS','publication/change-plan.md']),encoding='utf-8',newline='\n')
print(len(records),'files frozen; ZIP CRC passed')
