import json
with open('organisation/data.json') as f: d = json.load(f)
nodes = d['tree']['nodes']
ch = d['tree']['children']
node_names = {n['name'] for n in nodes}

orphan_parents = [p for p in ch if p not in node_names]
print(f"orphan parents (Reporting To name not in roster): {len(orphan_parents)}")
for p in sorted(orphan_parents, key=lambda p: -len(ch[p]))[:15]:
    print(f"  {p!r:40s}  ({len(ch[p])} reports)")
print()

# Cycle detection by component
visited_global = set()
def has_cycle_from(start):
    seen = set()
    in_stk = set()
    cyc = None
    def go(n):
        nonlocal cyc
        if n in in_stk:
            cyc = n
            return True
        if n in seen: return False
        seen.add(n); in_stk.add(n)
        for c in ch.get(n, []):
            if go(c): return True
        in_stk.remove(n); return False
    go(start)
    return cyc, seen

# Find all reporting cycles
print("Cycles found (Reporting-To loops):")
node_by_name = {n['name']: n for n in nodes}
seen_names = set()
for n in nodes:
    if n['name'] in seen_names: continue
    chain = []
    cur = n['name']
    local_seen = set()
    while cur and cur not in local_seen:
        local_seen.add(cur)
        chain.append(cur)
        nx = node_by_name.get(cur, {}).get('reportingTo')
        if not nx or nx == cur: break
        cur = nx
    if cur in local_seen and len(chain) > 1 and cur != chain[-1]:
        # cycle hit
        cycle_start = chain.index(cur)
        cyc = chain[cycle_start:] + [cur]
        if all(c not in seen_names for c in cyc):
            print(f"  cycle: {' -> '.join(cyc)}")
        seen_names.update(cyc)
    seen_names.update(local_seen)
