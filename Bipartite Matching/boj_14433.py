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


n, m, k1, k2 = map(int, input().split())
ans = 0

graph = [[] for _ in range(n + 1)]
for _ in range(k1):
    a, b = map(int, input().split())
    graph[a].append(b)

match = [0] * (m + 1)

for i in range(1, n + 1):
    visited = [0] * (m + 1)

    if dfs(i):
        ans += 1

graph = [[] for _ in range(n + 1)]
for _ in range(k2):
    a, b = map(int, input().split())
    graph[a].append(b)

match = [0] * (m + 1)

for i in range(1, n + 1):
    visited = [0] * (m + 1)

    if dfs(i):
        ans -= 1

if ans >= 0:
    print("그만 알아보자")
else:
    print("네 다음 힐딱이")

