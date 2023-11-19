from collections import deque

n, k = map(int, input().split())

arr = deque([i for i in range(1, n+1)])
ans = []

while arr:
    arr.rotate(1-k)
    ans.append(str(arr.popleft()))

print('<', ', '.join(ans), '>', sep='')

