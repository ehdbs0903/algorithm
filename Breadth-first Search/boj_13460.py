from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def move(x, y, direct):
    cnt = 0
    while graph[x + dx[direct]][y + dy[direct]] != '#' and graph[x][y] != 'O':
        x += dx[direct]
        y += dy[direct]
        cnt += 1

    return x, y, cnt


def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 1))

    while q:
        rx, ry, bx, by, cnt = q.popleft()
        visited[rx][ry][bx][by] = True

        if cnt > 10:
            print(-1)
            exit(0)

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, i)
            nbx, nby, bcnt = move(bx, by, i)

            if graph[nbx][nby] != 'O':
                if graph[nrx][nry] == 'O':
                    print(cnt)
                    exit(0)

                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, cnt + 1))

    print(-1)
    return


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            ri, rj = i, j
        if graph[i][j] == 'B':
            bi, bj = i, j

bfs(ri, rj, bi, bj)

