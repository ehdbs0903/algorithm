import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

relations = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
for _ in range(int(input())):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

q = deque()
q.append(a)
visited[a] = 0
while q:
    k = q.popleft()
    for i in range(len(relations[k])):
        if visited[relations[k][i]] == -1:
            visited[relations[k][i]] = visited[k] + 1
            q.append(relations[k][i])

print(visited[b])

