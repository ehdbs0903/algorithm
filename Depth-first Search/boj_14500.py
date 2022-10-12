import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, su, cnt):
    global ans

    if cnt == 4:
        ans = max(ans, su)
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if cnt == 2:
                visited[nx][ny] = 1
                dfs(x, y, su + graph[nx][ny], cnt + 1)
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, su + graph[nx][ny], cnt + 1)
            visited[nx][ny] = 0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = 0

print(ans)

