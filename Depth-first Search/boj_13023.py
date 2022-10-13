import sys

input = sys.stdin.readline


def dfs(v):
    if visited[v] >= 5:
        print(1)
        exit()

    for nv in friends[v]:
        if not visited[nv]:
            visited[nv] = visited[v] + 1
            dfs(nv)
            visited[nv] = 0


n, m = map(int, input().split())
friends = [[] for _ in range(n)]
visited = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(n):
    visited[i] = 1
    dfs(i)
    visited[i] = 0

print(0)
