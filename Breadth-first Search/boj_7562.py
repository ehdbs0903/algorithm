import sys
from collections import deque

input = sys.stdin.readline

dx = [2, 2, 1, -1, -2, -2, 1, -1]
dy = [1, -1, 2, 2, 1, -1, -2, -2]


def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1


for _ in range(int(input())):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    bfs(x1, y1)
    print(visited[x2][y2] - 1)

