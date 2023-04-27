from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def melt():
    nwt = deque()
    while water:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                nwt.append((nx, ny))
    return nwt


def bfs():
    t = deque()
    while swan:
        x, y = swan.popleft()
        if x == gol[0] and y == gol[1]:
            return True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    swan.append((nx, ny))
                else:
                    t.append((nx, ny))
    return t


n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
water = deque()
swan = deque()
graph = []
for i in range(n):
    s = input().rstrip()
    temp = []
    for j in range(m):
        if s[j] == 'L':
            swan.append((i, j))
            temp.append(-1)
            water.append((i, j))
        elif s[j] == '.':
            temp.append(0)
            water.append((i, j))
        else:
            temp.append(1)
    graph.append(temp)
gol = swan.pop()


con = 0
while True:
    water = melt()
    swan = bfs()
    if swan == True:
        print(con)
        break
    con += 1

