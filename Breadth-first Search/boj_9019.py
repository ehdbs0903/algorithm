import sys
from collections import deque

input = sys.stdin.readline


def operation_d(n):
    return 2 * n % 10000


def operation_s(n):
    return (n - 1) % 10000


def operation_l(n):
    return (n % 1000) * 10 + n // 1000


def operation_r(n):
    return (n % 10) * 1000 + n // 10


def bfs(a, b):
    operations = [operation_d, operation_s, operation_l, operation_r]
    labels = ['D', 'S', 'L', 'R']

    visited = [False] * 10000
    visited[a] = True

    q = deque([(a, '')])

    while q:
        v, path = q.popleft()
        if v == b:
            break

        for i, operation in enumerate(operations):
            nv = operation(v)

            if not visited[nv]:
                visited[nv] = True
                new_path = path + labels[i]
                q.append((nv, new_path))

    return path


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print(bfs(a, b))
