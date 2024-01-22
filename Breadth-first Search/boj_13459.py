import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
        elif board[i][j] == 'O':
            ax, ay = i, j


def move(rx, ry, bx, by, d):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    nrx, nry, nbx, nby = rx, ry, bx, by

    while board[nrx + dx[d]][nry + dy[d]] != '#':
        nrx += dx[d]
        nry += dy[d]
        if board[nrx][nry] == 'O':
            break

    while board[nbx + dx[d]][nby + dy[d]] != '#':
        nbx += dx[d]
        nby += dy[d]
        if board[nbx][nby] == 'O':
            break

    if board[nrx][nry] != 'O' and nrx == nbx and nry == nby:
        if abs(rx - nrx) + abs(ry - nry) > abs(bx - nbx) + abs(by - nby):
            nrx -= dx[d]
            nry -= dy[d]
        else:
            nbx -= dx[d]
            nby -= dy[d]

    return nrx, nry, nbx, nby


def bfs(rx, ry, bx, by):
    q = deque()
    q.append([rx, ry, bx, by])
    visited[rx][ry][bx][by] = 1

    while q:
        rx, ry, bx, by = q.popleft()

        for i in range(4):
            nrx, nry, nbx, nby = move(rx, ry, bx, by, i)
            if nbx == ax and nby == ay:
                continue

            if nrx == ax and nry == ay:
                return True

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = visited[rx][ry][bx][by] + 1

                if visited[nrx][nry][nbx][nby] <= 10:
                    q.append([nrx, nry, nbx, nby])

    return False


print(1 if bfs(rx, ry, bx, by) else 0)
