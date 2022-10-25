import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)

for _ in range(m):
    temp = list(map(int, input().split()))

    for i in range(2, len(temp)):
        graph[temp[i - 1]].append(temp[i])
        inDegree[temp[i]] += 1

q = deque()
for i in range(1, n + 1):
    if not inDegree[i]:
        q.append(i)

ans = []
while q:
    v = q.popleft()
    ans.append(v)

    for g in graph[v]:
        inDegree[g] -= 1

        if not inDegree[g]:
            q.append(g)

if len(ans) == n:
    for a in ans:
        print(a)

else:
    print(0)
