from collections import deque


n = int(input())
q = deque(map(int, input().split()))
s = []
k = 1

while q:
    if q and q[0] == k:
        q.popleft()
        k += 1
    else:
        s.append(q.popleft())

    while s and s[-1] == k:
        s.pop()
        k += 1

print("Sad" if s else "Nice")

