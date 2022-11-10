import sys

input = sys.stdin.readline
sys.setrecursionlimit(2000)


def dfs(v):
    for g in graph[v]:
        if not visited[g]:
            visited[g] = 1

            if not match[g] or dfs(match[g]):
                match[g] = v
                return True

    return False


n, m, k = map(int, input().split())
graph = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]

match = [0] * (m + 1)
ans = 0

for i in range(1, n + 1):
    visited = [0] * (m + 1)

    if dfs(i):
        ans += 1

for i in range(1, n + 1):
    while k > 0:
        visited = [0] * (m + 1)

        if dfs(i):
            ans += 1
            k -= 1
        else:
            break

print(ans)
