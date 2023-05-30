from collections import defaultdict

t = int(input())
n = int(input())
arrA = list(map(int, input().split()))
m = int(input())
arrB = list(map(int, input().split()))

sumA = defaultdict(int)

for i in range(n):
    s = 0
    for j in range(i, n):
        s += arrA[j]
        sumA[s] += 1

ans = 0
for i in range(m):
    s = 0
    for j in range(i, m):
        s += arrB[j]
        ans += sumA[t - s]

print(ans)
