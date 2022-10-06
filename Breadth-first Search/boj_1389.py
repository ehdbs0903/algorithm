import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    num = [0] * (n+1)
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        a = q.popleft()
        for i in relations[a]:
            if visited[i] == 0:
                num[i] = num[a]+1
                q.append(i)
                visited[i] = 1
    return sum(num)


n, m = map(int, input().split())
relations = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

result = []
for i in range(1, n + 1):
    visited = [0 for _ in range(n+1)]
    result.append(bfs(i))

print(result.index(min(result))+1)

