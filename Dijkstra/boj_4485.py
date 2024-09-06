import sys
import heapq

input = sys.stdin.readline


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = []

    heapq.heappush(q, (board[x][y], x, y))
    visited[x][y] = 1

    while q:
        w, x, y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            return w

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    heapq.heappush(q, (w + board[nx][ny], nx, ny))
                    visited[nx][ny] = 1


cnt = 1
while True:
    n = int(input())

    if n == 0:
        break

    board = [list(map(int, input().split()))for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    print("Problem ", cnt, ": ", bfs(0, 0), sep="")

    cnt += 1
