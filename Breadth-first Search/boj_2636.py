import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    global cnt
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny]:
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
                else:
                    q.append([nx, ny])
                    visited[nx][ny] = 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

time = 0
cnt = -1
ans = []
while cnt:
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    time += 1
    bfs(0, 0)
    ans.append(cnt)

print(time - 1)
print(ans[-2])

