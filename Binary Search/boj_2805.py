n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    height = 0
    for t in trees:
        diff = t - mid
        if diff < 0:
            diff = 0
        height += diff

    if height >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
