import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[x][y] == '*':
                    if graph[nx][ny] == '.' or graph[nx][ny] == 'S':
                        graph[nx][ny] = '*'
                        q.append([nx, ny])
                else:
                    move[nx][ny] = move[x][y] + 1
                    if graph[nx][ny] == '.':
                        graph[nx][ny] = 'S'
                        q.append([nx, ny])
                    elif graph[nx][ny] == 'D':
                        print(move[ans_x][ans_y])
                        exit(0)


r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
move = [[0] * c for _ in range(r)]

q = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            q.append([i, j])
        elif graph[i][j] == 'S':
            q.appendleft([i, j])
        elif graph[i][j] == 'D':
            ans_x, ans_y = i, j

bfs()
print("KAKTUS")

