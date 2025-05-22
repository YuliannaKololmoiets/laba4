def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

def union(parent, rank, u, v):
    u_root = find(parent, u)
    v_root = find(parent, v)
    if u_root == v_root:
        return False
    if rank[u_root] < rank[v_root]:
        parent[u_root] = v_root
    else:
        parent[v_root] = u_root
        if rank[u_root] == rank[v_root]:
            rank[u_root] += 1
    return True

n, m = map(int, input().split())
edges = []

for idx in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u - 1, v - 1, idx + 1))  
edges.sort()

parent = [i for i in range(n)]
rank = [0] * n

mst_weight = 0
mst_edges = []

for w, u, v, idx in edges:
    if union(parent, rank, u, v):
        mst_weight += w
        mst_edges.append(idx)
        if len(mst_edges) == n - 1:
            break

if len(mst_edges) != n - 1:
    print(-1)
else:
    print(mst_weight)
    for e in sorted(mst_edges):
        print(e)

