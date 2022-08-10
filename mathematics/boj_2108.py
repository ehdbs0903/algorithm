import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

k = Counter(arr).most_common()

print(round(sum(arr)/n))
print(arr[n//2])
if len(arr) > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(k[0][0])
else:
    print(arr[0])
print(max(arr) - min(arr))
