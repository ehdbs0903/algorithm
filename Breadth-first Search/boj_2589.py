import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    global ans
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
                ans = max(ans, visited[nx][ny])


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

answer = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            ans = 0
            bfs(i, j)
            answer.append(ans)

print(max(answer) - 1)

