import sys
from collections import deque

input = sys.stdin.readline


def bfs(v):
    visited = [0] * 101
    visited[v] = 1

    q = deque()
    q.append(v)

    while q:
        v = q.popleft()

        for i in range(1, 7):
            nv = v + i

            if nv <= 100 and not visited[nv]:
                visited[nv] = visited[v] + 1
                
                nnv = board[nv]
                if board[nv]:
                    if not visited[nnv]:
                        visited[nnv] = visited[nv]
                        q.append(nnv)
                else:
                    q.append(nv)

    return visited[100]


n, m = map(int, input().split())

board = [0] * 101
for _ in range(n + m):
    start, end = map(int, input().split())
    board[start] = end

print(bfs(1)-1)
