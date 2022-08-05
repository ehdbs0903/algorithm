import sys

input = sys.stdin.readline

t = int(input())

P = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(t):
    n = int(input())
    if n <= len(P):
        print(P[n-1])
    else:
        for i in range(len(P)-1, n-1):
            P.append(P[i]+P[i-4])
        print(P[n-1])
