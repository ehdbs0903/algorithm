import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [1e9] * (n + 1)
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])


def dijkstra(v):
    heap = []
    heapq.heappush(heap, (0, v))
    visited[v] = 0

    while heap:
        c, v = heapq.heappop(heap)

        if visited[v] < c:
            continue

        for nv, w in graph[v]:
            nc = c + w

            if visited[nv] > nc:
                heapq.heappush(heap, (nc, nv))
                visited[nv] = nc


start, end = map(int, input().split())
dijkstra(start)
print(visited[end])

