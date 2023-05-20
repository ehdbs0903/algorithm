import sys

input = sys.stdin.readline


def gcd(a, b):
    while b:
        if a > b:
            a, b = b, a
        b %= a
    return a


distance = []
n = int(input())

pos = int(input())
for _ in range(n - 1):
    temp = int(input())
    distance.append(temp - pos)
    pos = temp

cd = distance[0]
for i in range(1, n - 1):
    cd = gcd(cd, distance[i])

res = 0
for d in distance:
    res += d // cd - 1

print(res)