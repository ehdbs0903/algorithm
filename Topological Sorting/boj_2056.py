import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]

    for j in range(2, len(temp)):
        graph[i].append(temp[j])
        inDegree[temp[j]] += 1

q = deque()
for i in range(1, n + 1):
    if not inDegree[i]:
        q.append(i)

ans = [0] * (n + 1)
while q:
    v = q.popleft()
    ans[v] += time[v]

    for g in graph[v]:
        inDegree[g] -= 1
        ans[g] = max(ans[v], ans[g])

        if not inDegree[g]:
            q.append(g)

print(max(ans))

