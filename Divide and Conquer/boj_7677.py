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
            C[i][j] %= 10000
    return C


if __name__ == "__main__":
    A = [[1, 1], [1, 0]]

    while True:
        n = int(input())
        
        if n == -1:
            break
        elif n == 0:
            print(0)
        else:
            ans = square(A, n)[0][1]
            print(ans)
