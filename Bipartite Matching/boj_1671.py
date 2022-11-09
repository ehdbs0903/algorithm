import sys

input = sys.stdin.readline


def dfs(v):
    for g in graph[v]:
        if not visited[g]:
            visited[g] = 1

            if match[g] == -1 or dfs(match[g]):
                match[g] = v
                return True

    return False


n = int(input())
shark = [list(map(int, input().split())) for i in range(n)]

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if shark[i][0] == shark[j][0] and shark[i][1] == shark[j][1] and shark[i][2] == shark[j][2] and i > j:
            continue
        if shark[i][0] >= shark[j][0] and shark[i][1] >= shark[j][1] and shark[i][2] >= shark[j][2]:
            graph[i].append(j)

match = [-1] * n
ans = 0

for i in range(2):
    for j in range(n):
        visited = [0] * n

        if dfs(j):
            ans += 1

print(n - ans)

