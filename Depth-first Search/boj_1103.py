import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global ans
    ans = max(ans, dp[x][y])
    a = int(graph[x][y])

    for i in range(4):
        nx, ny = x + dx[i] * a, y + dy[i] * a

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'H' and dp[x][y] >= dp[nx][ny]:
            if visited[nx][ny]:
                print(-1)
                exit()

            visited[nx][ny] = 1
            dp[nx][ny] = dp[x][y] + 1
            dfs(nx, ny)
            visited[nx][ny] = 0


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
ans = 0

visited[0][0] = 1
dp[0][0] = 1
dfs(0, 0)

print(ans)

