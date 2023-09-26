import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, w = map(int, input().split())
    graph[start].append([end, w])


def dijkstra(v):
    visited = [1e9] * (n+1)
    visited[v] = 0
    heap = [[0, v]]

    while heap:
        c, v = heapq.heappop(heap)

        if c > visited[v]:
            continue

        for nv, w in graph[v]:
            nc = c + w
            if nc < visited[nv]:
                visited[nv] = nc
                heapq.heappush(heap, [nc, nv])

    return visited


ans = 0
dij1 = dijkstra(x)
for i in range(1, n+1):
    if i == x:
        continue

    dij2 = dijkstra(i)
    ans = max(ans, dij2[x] + dij1[i])

print(ans)

