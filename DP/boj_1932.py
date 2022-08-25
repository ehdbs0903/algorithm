import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.append([0] * (n+1))

for i in range(1, len(arr)):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][0] += arr[i-1][0]
        elif j == len(arr[i])-1:
            arr[i][-1] += arr[i-1][-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[-1]))
