int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0

for i in range(n):
    temp = a[:i] + a[i + 1:]
    left, right = 0, len(temp) - 1

    while left < right:
        target = temp[left] + temp[right]

        if target == a[i]:
            ans += 1
            break

        if target < a[i]:
            left += 1
        else:
            right -= 1

print(ans)
