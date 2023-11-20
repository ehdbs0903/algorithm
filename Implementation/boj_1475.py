num = input()

arr = [0] * 10

for n in num:
    arr[int(n)] += 1

arr[6] = arr[9] = round((arr[6] + arr[9] + 1) // 2)

print(max(arr))
