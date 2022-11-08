import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    inDegree = [0] * (n + 1)

    for i in range(n):
        for j in range(i + 1, n):
            graph[arr[i]].append(arr[j])
            inDegree[arr[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        if b in graph[a]:
            graph[a].remove(b)
            inDegree[b] -= 1
            graph[b].append(a)
            inDegree[a] += 1

        else:
            graph[b].remove(a)
            inDegree[a] -= 1
            graph[a].append(b)
            inDegree[b] += 1

    q = deque()
    for i in range(1, n + 1):
        if graph[i] and not inDegree[i]:
            q.append(i)

    ans = []
    while q:
        v = q.popleft()
        ans.append(v)

        for g in graph[v]:
            inDegree[g] -= 1

            if not inDegree[g]:
                q.append(g)

    if len(ans) < n:
        print("IMPOSSIBLE")
    else:
        print(*ans)

