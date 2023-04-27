from collections import deque

dx = [0, -1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 0, -1, 1, 1, -1, 1, -1]

graph = [list(input()) for _ in range(8)]

q = deque()
q.append([7, 0])

while q:
    visited = [[0] * 8 for _ in range(8)]

    for _ in range(len(q)):
        x, y = q.popleft()

        if x == 0 and y == 7:
            print(1)
            exit()

        if graph[x][y] == '#':
            continue

        for i in range(9):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 8 and 0 <= ny < 8 and graph[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])

    for i in range(7, -1, -1):
        for j in range(8):
            if graph[i][j] == '#':
                graph[i][j] = '.'
                if i < 7:
                    graph[i + 1][j] = '#'

print(0)

