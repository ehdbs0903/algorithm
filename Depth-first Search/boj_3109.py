import sys

input = sys.stdin.readline


dx = [-1, 0, 1]

r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]

visited = [[0] * c for _ in range(r)]
cnt = 0


def dfs(x, y):
    if y == c - 1:
        return 1

    for i in range(3):
        nx, ny = x + dx[i], y + 1

        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] == '.':
            visited[nx][ny] = 1
            if dfs(nx, ny) == 1:
                return 1
    return 0


for i in range(r):
    cnt += dfs(i, 0)

print(cnt)

