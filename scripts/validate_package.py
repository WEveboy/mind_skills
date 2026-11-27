"""Check self-contained package links and optional frozen public manifest."""
from pathlib import Path
import hashlib,json,re,shutil,tempfile
root=Path(__file__).resolve().parents[1]
skill=root/'skills/mind_skill'
with tempfile.TemporaryDirectory() as temp:
 target=Path(temp)/'mind_skill';shutil.copytree(skill,target)
 entry=(target/'SKILL.md').read_text(encoding='utf-8')
 assert entry.startswith('---\nname: mind_skill\n')
 count=0
 for p in target.rglob('*.md'):
  text=p.read_text(encoding='utf-8')
  for link in re.findall(r'\]\(([^)]+)\)',text):
   if '://' in link:continue
   resolved=(p.parent/link.split('#')[0]).resolve()
   assert resolved.is_relative_to(target.resolve()),(p,link,'escapes package')
   assert resolved.exists(),(p,link)
   count+=1
  assert not re.search(r'[A-Z]:[/\\]Users[/\\]',text),p
 print('isolated copy: entrypoint and',count,'relative links passed')
manifest=root/'publication/PUBLIC_MANIFEST.json'
if manifest.exists():
 data=json.loads(manifest.read_text(encoding='utf-8'))
 for f in data['files']:
  b=(root/f['path']).read_bytes()
  assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256'],f['path']
 print('frozen public manifest:',len(data['files']),'files matched')
print('User-specified underscore name retained; generic hyphen-only naming check is an explicit exception.')
