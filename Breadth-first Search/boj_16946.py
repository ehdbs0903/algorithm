import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global group
    q = deque()
    q.append([x, y])
    visited[x][y] = group
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '0' and not visited[nx][ny]:
                visited[nx][ny] = group
                q.append([nx, ny])

    return cnt


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
groups = {}

group = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0' and not visited[i][j]:
            groups[group] = bfs(i, j)
            group += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            temp_groups = set()

            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]

                if 0 <= ni < n and 0 <= nj < m and visited[ni][nj]:
                    temp_groups.add(visited[ni][nj])

            ans = 1
            for g in temp_groups:
                ans += groups[g]

            graph[i][j] = str(ans % 10)

for g in graph:
    print("".join(g))

