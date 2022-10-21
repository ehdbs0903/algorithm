import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)

q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, n + 1):
    if not inDegree[i]:
        q.append(i)

while q:
    temp = q.popleft()
    print(temp, end=' ')

    for i in graph[temp]:
        inDegree[i] -= 1

        if not inDegree[i]:
            q.append(i)

