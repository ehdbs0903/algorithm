import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
visited = [200001] * (v+1)
for _ in range(e):
    start, end, w = map(int, input().split())
    graph[start].append((end, w))


def dijkstra(v):
    heap = [(0, v)]
    visited[v] = 0
    while heap:
        c, v = heapq.heappop(heap)

        if visited[v] < c:
            continue

        for nv, w in graph[v]:
            nc = c + w

            if nc < visited[nv]:
                visited[nv] = nc
                heapq.heappush(heap, (nc, nv))


dijkstra(k)
for i in range(1, (v+1)):
    print(visited[i] if visited[i] != 200001 else "INF")

