import sys
from collections import deque

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())

    if not n and not m:
        break

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

    ans = []
    while q:
        temp = q.popleft()
        ans.append(temp)

        for i in graph[temp]:
            inDegree[i] -= 1

            if not inDegree[i]:
                q.append(i)

    if len(ans) == n:
        for a in ans:
            print(a)
    else:
        print("IMPOSSIBLE")

