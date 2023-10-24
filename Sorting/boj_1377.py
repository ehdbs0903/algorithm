import sys

input = sys.stdin.readline

n = int(input())
arr = [(int(input()), i) for i in range(n)]

sorted_arr = sorted(arr)

ans = 0
for i in range(n):
    ans = max(ans, sorted_arr[i][1] - arr[i][1])

print(ans + 1)

