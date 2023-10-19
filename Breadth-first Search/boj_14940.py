import sys
from collections import deque


input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] or board[nx][ny] != 1:
                    continue

                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])


n, m = map(int, input().split())

board = []
flag = 0
for i in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)

    if flag:
        continue

    for j in range(m):
        if temp[j] == 2:
            start_x, start_y = i, j
            flag = 1

visited = [[0] * m for _ in range(n)]

bfs(start_x, start_y)

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            visited[i][j] = -1

for v in visited:
    print(*v)

