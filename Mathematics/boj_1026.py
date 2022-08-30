n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()
a.sort(reverse = True)

s = 0
for i in range(n):
    s += a[i] * b[i]

print(s)
