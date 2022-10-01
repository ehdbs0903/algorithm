n = int(input())

su = 0
for i in range(1, n + 1):
    su += (n // i) * i

print(su)

