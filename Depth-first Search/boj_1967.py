import sys

input = sys.stdin.readline
sys.setrecursionlimit(10001)


def dfs(v, w):
    global distance, farthest_node

    visited[v] = True

    if distance < w:
        distance = w
        farthest_node = v

    for nv, nw in graph[v]:
        if not visited[nv]:
            dfs(nv, w + nw)


n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])


farthest_node = 1
distance = 0
visited = [False] * (n+1)
dfs(1, 0)

distance = 0
visited = [False] * (n+1)
dfs(farthest_node, 0)

print(distance)
