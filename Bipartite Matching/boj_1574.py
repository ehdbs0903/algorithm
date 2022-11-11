import sys

input = sys.stdin.readline


def dfs(v):
    for g in graph[v]:
        if g and not visited[g]:
            visited[g] = 1

            if not match[g] or dfs(match[g]):
                match[g] = v
                return True

    return False


r, c, n = map(int, input().split())
blank = [list(map(int, input().split())) for _ in range(n)]

graph = [[]] + [[0] + [i for i in range(1, c + 1)] for _ in range(1, r + 1)]
for x, y in blank:
    graph[x][y] = 0

match = [0] * (c + 1)
ans = 0

for i in range(1, r + 1):
    visited = [0] * (c + 1)
    ans += dfs(i)

print(ans)
