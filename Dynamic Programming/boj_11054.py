n = int(input())

nums = list(map(int, input().split()))

asc = [0] * n
dsc = [0] * n
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and asc[i] < asc[j]:
            asc[i] = asc[j]
    asc[i] += 1
for i in reversed(range(n)):
    for j in range(n-1, i, -1):
        if nums[i] > nums[j] and dsc[i] < dsc[j]:
            dsc[i] = dsc[j]
    dsc[i] += 1
print(max(map(sum, zip(asc, dsc)))-1)
