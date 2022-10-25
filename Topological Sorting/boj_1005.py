import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    inDegree = [0] * (n + 1)

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        inDegree[y] += 1

    q = deque()
    for i in range(1, n + 1):
        if not inDegree[i]:
            q.append(i)

    ans = [0] * (n + 1)
    while q:
        v = q.popleft()
        ans[v] += d[v]

        for g in graph[v]:
            inDegree[g] -= 1
            ans[g] = max(ans[v], ans[g])

            if not inDegree[g]:
                q.append(g)

    w = int(input())
    print(ans[w])

