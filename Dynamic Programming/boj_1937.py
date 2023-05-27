import sys

input = sys.stdin.readline

n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if visited[x][y]:
        return visited[x][y]

    visited[x][y] = 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and board[x][y] < board[nx][ny]:
            visited[x][y] = max(visited[x][y], dfs(nx, ny) + 1)

    return visited[x][y]


max_value = 0
for i in range(n):
    for j in range(n):
        max_value = max(max_value, dfs(i, j))

print(max_value)