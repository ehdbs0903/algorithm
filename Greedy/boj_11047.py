import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []

cnt = 0
for _ in range(n):
    coins.append(int(input()))

for i in reversed(coins):
    cnt += k // i
    k -= i * (k // i)

print(cnt)
