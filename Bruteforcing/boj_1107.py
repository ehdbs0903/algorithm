target = int(input())
m = int(input())

if m:
    broken = set(input().split())
else:
    broken = set()

ans = abs(100 - target)
for num in range(1000001):
    for n in str(num):
        if n in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)

