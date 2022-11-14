import sys

input = sys.stdin.readline

dx = [-1, 0, 1, -1, 0, 1]
dy = [-1, -1, -1, 1, 1, 1]


def dfs(v):
    visited[v] = ans

    for g in graph[v]:
        if visited[g] != ans:
            visited[g] = ans

            if not match[g] or dfs(match[g]):
                match[g] = v
                match[v] = g
                return True

    return False


for _ in range(int(input())):
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]

    graph = [[] for _ in range(n * m + 1)]

    total = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                total += 1

                for k in range(6):
                    nx, ny = i + dx[k], j + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.':
                        graph[i * m + j + 1].append(nx * m + ny + 1)

    match = [0] * (n * m + 1)
    visited = [-1] * (n * m + 1)
    ans = 0

    for i in range(1, n * m + 1):
        if not match[i]:
            ans += dfs(i)

    print(total - ans)

