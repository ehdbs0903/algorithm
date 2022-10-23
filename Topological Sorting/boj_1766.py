import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

q = []
for i in range(1, n + 1):
    if not inDegree[i]:
        heapq.heappush(q, i)

while q:
    temp = heapq.heappop(q)

    for g in graph[temp]:
        inDegree[g] -= 1

        if not inDegree[g]:
            heapq.heappush(q, g)

    print(temp, end=' ')

