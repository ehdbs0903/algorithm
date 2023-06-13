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
    C = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= p
    return C


n = int(input())

p = 1000000007
A = [[1, 1], [1, 0]]

tmp = square(A, n)
print((tmp[0][0] ** 2 - tmp[0][1] ** 2 + (-1) ** (n + 1) + p) % p)
