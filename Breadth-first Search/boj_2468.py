import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > h and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = []
for h in range(101):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    answer.append(cnt)
    if cnt == 0:
        break

print(max(answer))
