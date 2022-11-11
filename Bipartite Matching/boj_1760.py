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
board = [list(map(int, input().split())) for _ in range(n)]

row = [[0] * m for _ in range(n)]
col = [[0] * m for _ in range(n)]

cnt = 1
r = 0
for i in range(n):
    flag = 0

    for j in range(m):
        if board[i][j] == 2:
            if flag:
                cnt += 1
                flag = 0

        else:
            row[i][j] = cnt
            r = cnt
            flag = 1

    if flag:
        cnt += 1

cnt = 1
c = 0
for j in range(m):
    flag = 0

    for i in range(n):
        if board[i][j] == 2:
            if flag:
                cnt += 1
                flag = 0

        else:
            col[i][j] = cnt
            c = cnt
            flag = 1

    if flag:
        cnt += 1

graph = [[] for _ in range(r + 1)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            graph[row[i][j]].append(col[i][j])

match = [0] * (c + 1)
ans = 0
for i in range(1, r + 1):
    visited = [0] * (c + 1)
    ans += dfs(i)

print(ans)
