import sys

input = sys.stdin.readline


def dfs(v):
    for g in graph[v]:
        if not visited[g]:
            visited[g] = 1

            if not match[g] or dfs(match[g]):
                match[g] = v
                return True

    return False


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(1, m + 1):
    a, b = map(int, input().split())
    graph[a].append(b)

match = [0] * (n + 1)
ans = 0

for i in range(1, n + 1):
    visited = [0] * (n + 1)

    if dfs(i):
        ans += 1

print(ans)

