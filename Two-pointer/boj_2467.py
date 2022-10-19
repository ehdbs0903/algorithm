n = int(input())
arr = list(map(int, input().split()))

start, end = 0, n - 1
left, right = arr[0], arr[1]
while start < end < n:
    sum = arr[start] + arr[end]

    if abs(sum) < abs(left + right):
        left, right = arr[start], arr[end]

    if sum == 0:
        break
    elif sum > 0:
        end -= 1
    else:
        start += 1

print(left, right)

