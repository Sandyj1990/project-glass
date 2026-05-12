import json
with open('organisation/data.json') as f: d = json.load(f)
nodes = d['tree']['nodes']
ch = d['tree']['children']

# DFS from roots with cycle protection that doesn't abort
def reachable(roots, ch):
    seen = set()
    stack = list(roots)
    while stack:
        n = stack.pop()
        if n in seen: continue
        seen.add(n)
        for c in ch.get(n, []):
            if c not in seen:
                stack.append(c)
    return seen

reach = reachable(d['tree']['rootNames'], ch)
print(f"reachable from roots: {len(reach)} / {len(nodes)}")
print(f"unreachable: {len(nodes) - len(reach)}")
print()
# What's the largest unreachable subtree? Find connected components.
node_names = {n['name'] for n in nodes}
unreach = node_names - reach
# Build a children-or-parent adjacency for component analysis
parents = {}
for parent, kids in ch.items():
    for k in kids:
        parents[k] = parent

# Find someone in unreachable, walk up via reportingTo, see where they top out
node_by_name = {n['name']: n for n in nodes}
def trace_up(name, max_steps=50):
    path = [name]
    seen = {name}
    for _ in range(max_steps):
        n = node_by_name.get(path[-1])
        if not n: break
        rt = n.get('reportingTo')
        if not rt or rt == path[-1] or rt in seen:
            if rt and rt in seen: path.append(f"(loops to {rt})")
            break
        path.append(rt); seen.add(rt)
    return path

print("Sample unreachable people, traced up via reportingTo:")
for s in list(unreach)[:5]:
    print(f"  {s}: {' -> '.join(trace_up(s)[:8])}{'...' if len(trace_up(s)) > 8 else ''}")
