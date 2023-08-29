import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    wall[x][y] = 0
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and wall[nx][ny] == -1:
                if board[nx][ny] == '0':
                    wall[nx][ny] = wall[x][y]
                    q.appendleft([nx, ny])
                else:
                    wall[nx][ny] = wall[x][y] + 1
                    q.append([nx, ny])


if __name__ == '__main__':
    m, n = map(int, input().split())
    board = [input() for _ in range(n)]

    wall = [[-1] * m for _ in range(n)]
    bfs(0, 0)
    print(wall[n-1][m-1])

