import heapq
from collections import defaultdict
#gasstations
def min_cost_to_reach_last_city(n, fuel_costs, roads):
    graph = defaultdict(list)
    for u, v in roads:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

   
    dist = [float('inf')] * n
    dist[0] = 0 
    heap = [(0, 0)]

    while heap:
        cost, u = heapq.heappop(heap)
        if cost > dist[u]:
            continue
        for v in graph[u]:
            new_cost = dist[u] + fuel_costs[u]
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(heap, (new_cost, v))

    return dist[n - 1] if dist[n - 1] != float('inf') else -1

n = int(input())
fuel_costs = list(map(int, input().split()))
m = int(input())
roads = [tuple(map(int, input().split())) for _ in range(m)]

print(min_cost_to_reach_last_city(n, fuel_costs, roads))

