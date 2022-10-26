import sys
from collections import deque

input = sys.stdin.readline

for _ in range(1, int(input()) + 1):
    k, m, p = map(int, input().split())

    graph = [[] for _ in range(m + 1)]
    inDegree = [0] * (m + 1)

    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1

    q = deque()
    for i in range(1, m + 1):
        if not inDegree[i]:
            q.append(i)

    cnt = [0] * (m + 1)
    strahler = [[1, 1] for _ in range(m + 1)]

    while q:
        v = q.popleft()

        if cnt[v] >= 2:
            strahler[v][0] += 1

        for g in graph[v]:
            inDegree[g] -= 1

            if strahler[g][0] == strahler[v][0]:
                cnt[g] += 1
            elif strahler[g][1] < strahler[v][0]:
                strahler[g][0] = strahler[v][0]
                cnt[g] = 1

            if not inDegree[g]:
                q.append(g)

    print(k, strahler[m][0])

