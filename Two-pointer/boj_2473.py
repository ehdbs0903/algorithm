n = int(input())
arr = sorted(list(map(int, input().split())))

ans_sum = 3000000001
for i in range(n - 2):
    left, right = i + 1, n - 1

    while left < right:
        temp_sum = arr[i] + arr[left] + arr[right]

        if ans_sum > abs(temp_sum):
            ans_sum = abs(temp_sum)
            ans = [arr[i], arr[left], arr[right]]

        if temp_sum == 0:
            print(*ans)
            exit(0)
        elif temp_sum > 0:
            right -= 1
        else:
            left += 1

print(*ans)

