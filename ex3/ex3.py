import heapq

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
min_edge = [float('inf')] * n
parent = [-1] * n

min_edge[0] = 0
pq = [(0, 0)] 

total_weight = 0
result_edges = []

while pq:
    weight, u = heapq.heappop(pq)
    if visited[u]:
        continue
    visited[u] = True
    total_weight += weight

    if parent[u] != -1:
        result_edges.append((parent[u] + 1, u + 1))

    for v in range(n):
        if graph[u][v] != 0 and not visited[v] and graph[u][v] < min_edge[v]:
            min_edge[v] = graph[u][v]
            parent[v] = u
            heapq.heappush(pq, (graph[u][v], v))

if not all(visited):
    print(-1)
else:
    print(total_weight)
    for u, v in result_edges:
        print(u, v)

