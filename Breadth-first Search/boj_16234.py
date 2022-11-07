import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    num.append([x, y])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    num.append([nx, ny])


n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

day = 0
while True:
    visited = [[0] * n for _ in range(n)]
    nums = []
    num = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                if len(num) > 1:
                    nums.append(num)
                num = []

    if not len(nums):
        break

    for nu in nums:
        avg = 0
        for nn in nu:
            avg += graph[nn[0]][nn[1]]
        avg //= len(nu)
        for nn in nu:
            graph[nn[0]][nn[1]] = avg

    day += 1

print(day)

