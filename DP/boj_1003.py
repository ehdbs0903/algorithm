import sys

input = sys.stdin.readline

t = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]

def fibo(n):
    l = len(zero)
    if n >= l:
        for i in range(l, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[n], one[n]))

for i in range(t):
    n = int(input())
    fibo(n)
