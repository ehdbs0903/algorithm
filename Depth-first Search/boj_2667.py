import sys

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(input().rstrip())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    global cnt

    if graph[x][y] == '1':
        graph[x] = graph[x][:y] + '0' + graph[x][y+1:]
        cnt += 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True
    return False

result = 0
cnt = 0
count = []
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            count.append(cnt)
            result += 1
            cnt = 0
count.sort()
print(result)
for i in count:
    print(i)
