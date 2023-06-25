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
    C = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= 1000000007
    return C


def gcd(a, b):
    while a:
        b %= a
        a, b = b, a
    return b


if __name__ == "__main__":
    A = [[1, 1], [1, 0]]

    for _ in range(int(input())):
        n, m = map(int, input().split())

        gcd_nm = gcd(n, m)
        ans = square(A, gcd_nm)[0][1]

        print(ans)