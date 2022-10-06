import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny] and not visited[nx][ny][w]:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])

                elif graph[nx][ny] and not w:
                    visited[nx][ny][w + 1] = visited[x][y][w] + 1
                    q.append([nx, ny, w + 1])


n, m = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

bfs()

if min(visited[-1][-1]) != 0:
    answer = min(visited[-1][-1])
else:
    answer = max(visited[-1][-1])

if answer:
    print(answer)
else:
    print(-1)

