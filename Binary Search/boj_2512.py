n = int(input())
required = list(map(int, input().split()))
m = int(input())

start, end = m // n, max(required)

while start <= end:
    mid = (start + end) // 2
    budget = 0
    for re in required:
        budget += min(mid, re)

    if budget <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
