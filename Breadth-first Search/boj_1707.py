import sys
from collections import deque

input = sys.stdin.readline


def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1

    while q:
        n = q.popleft()
        for nv in graph[n]:
            if not visited[nv]:
                q.append(nv)
                if visited[n] == 2:
                    visited[nv] = 1
                else:
                    visited[nv] = 2
            else:
                if visited[n] == visited[nv]:
                    return 0
    return 1


for _ in range(int(input())):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (V + 1)

    flag = 1
    for j in range(1, V + 1):
        if not visited[j]:
            flag = bfs(j)
            if not flag:
                break

    if flag:
        print("YES")
    else:
        print("NO")

