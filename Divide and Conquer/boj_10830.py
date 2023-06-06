import sys

input = sys.stdin.readline


def square(A, n):
    if n == 1:
        return A
    else:
        temp = square(A, n//2)
        ret = multi_matrix(temp, temp)
        if n % 2:
            return multi_matrix(ret, A)
        else:
            return ret


def multi_matrix(A, B):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= 1000
    return C


n, b = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if A[i][j] == 1000:
            A[i][j] = 0

ans = square(A, b)
for a in ans:
    print(*a)
