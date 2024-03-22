import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[0] * m for _ in range(n)]
    cnt = 0  # 만날 수 있는 사람의 수

    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):  # 상하좌우 탐색
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny])

                    if board[nx][ny] == 'P':
                        cnt += 1  # 사람 만날 때마다 카운트 증가
    return cnt


n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            start_x, start_y = i, j  # 시작 위치
            break

ans = bfs(start_x, start_y)
print(ans if ans else "TT")  # 만난 사람이 없으면 "TT" 출력
