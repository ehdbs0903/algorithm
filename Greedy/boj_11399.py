n = int(input())

p = list(map(int, input().split()))
p.sort()
for i in range(n-1):
    p[i+1] += p[i]
print(sum(p))
