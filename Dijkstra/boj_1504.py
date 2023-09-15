import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b ,c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())


def dijkstra(v):
    visited = [1e9] * (n + 1)
    heap = []
    heap.append((0, v))
    visited[v] = 0

    while heap:
        w, v = heapq.heappop(heap)

        if w > visited[v]:
            continue

        for nv, nw in graph[v]:
            if w + nw < visited[nv]:
                heapq.heappush(heap, (w+nw, nv))
                visited[nv] = visited[v] + nw

    return visited


v_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)
path1 = v_dist[v1] + v1_dist[v2] + v2_dist[n]
path2 = v_dist[v2] + v2_dist[v1] + v1_dist[n]
path = min(path1, path2)
print(path if path < 1e9 else -1)

