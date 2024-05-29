from collections import deque

n = int(input())

queue = deque([i for i in range(1, n+1)])

while n > 1:
    queue.popleft()
    queue.append(queue.popleft())
    n -= 1

print(queue[0])
