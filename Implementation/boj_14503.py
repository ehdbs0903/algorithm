N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def clean(r, c, d):
    global answer
    if room[r][c] == 0:
        room[r][c] = 2
        answer += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx, ny = r + dx[nd], c + dy[nd]
        if room[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx, ny = r + dx[nd], c + dy[nd]
    if room[nx][ny] != 1:
        clean(nx, ny, d)


answer = 0
clean(r, c, d)
print(answer)

