import json, openpyxl, warnings
warnings.filterwarnings('ignore')
wb = openpyxl.load_workbook('docs/org-notes-compilation/Team List Billed v2.xlsx', data_only=True, read_only=True)
s = wb['Trupti -Updated Employee Master']
rows = list(s.iter_rows(values_only=True))
hdr = rows[0]
PCOL = hdr.index('Project'); TCOL = hdr.index('Track')
with open('organisation/mappings.json') as f: m = json.load(f)
mapped_tracks = {k.lower() for k in m['tracks']}
mapped_projects = set(m['projects'].keys())
unmapped_tracks = set()
unmapped_projects = set()
for r in rows[1:]:
    p = (r[PCOL] or '').strip()
    t = (r[TCOL] or '').strip()
    if p and p not in mapped_projects:
        unmapped_projects.add(p)
    if t and t.lower() not in mapped_tracks:
        unmapped_tracks.add(t)
print('UNMAPPED PROJECTS:')
for p in sorted(unmapped_projects):
    print(f'  {p!r}')
print()
print('UNMAPPED TRACKS:')
for t in sorted(unmapped_tracks):
    print(f'  {t!r}')
