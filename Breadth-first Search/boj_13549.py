import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    graph[x][y] = 1
    global area
    while q:
        x, y = q.popleft()
        area += 1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < m and 0 <= ny < n and not graph[nx][ny]:
                q.append([nx, ny])
                graph[nx][ny] = 1


m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]
answer = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

area = 0
for i in range(m):
    for j in range(n):
        if not graph[i][j]:
            bfs(i, j)
            answer.append(area)
            area = 0

answer.sort()
print(len(answer))
print(*answer)

