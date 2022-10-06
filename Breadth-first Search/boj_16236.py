import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and size >= graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
                if graph[nx][ny] and graph[nx][ny] < size:
                    possible.append([visited[nx][ny], nx, ny])


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
time = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            x, y = i, j

size = 2
cnt = 0
while True:
    visited = [[0] * n for _ in range(n)]
    possible = []
    bfs(x, y)
    if len(possible) == 0:
        break
    possible.sort(key=lambda z: (z[0], z[1], z[2]))
    x, y = possible[0][1], possible[0][2]
    graph[x][y] = 0
    time += visited[x][y]
    cnt += 1
    if size == cnt:
        size += 1
        cnt = 0

print(time)

