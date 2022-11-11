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


n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

row = [[0] * n for _ in range(n)]
col = [[0] * n for _ in range(n)]

cnt = 1
r = 0
for i in range(n):
    flag = 0

    for j in range(n):
        if board[i][j] == '.':
            col[i][j] = cnt
            r = cnt
            flag = 1

        else:
            if flag:
                cnt += 1
                flag = 0

    if flag:
        cnt += 1

cnt = 1
c = 0
for j in range(n):
    flag = 0

    for i in range(n):
        if board[i][j] == '.':
            row[i][j] = cnt
            c = cnt
            flag = 1

        else:
            if flag:
                cnt += 1
                flag = 0

    if flag:
        cnt += 1

graph = [[] for _ in range(r + 1)]
for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            graph[row[i][j]].append(col[i][j])

match = [0] * (c + 1)
ans = 0

for i in range(1, r + 1):
    visited = [0] * (c + 1)
    ans += dfs(i)

print(ans)
