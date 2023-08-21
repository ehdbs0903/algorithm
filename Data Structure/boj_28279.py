from collections import deque
import sys

input = sys.stdin.readline

deq = deque()

for _ in range(int(input())):
    temp = list(map(int, input().split()))

    if temp[0] == 1:
        deq.appendleft(temp[1])
    elif temp[0] == 2:
        deq.append(temp[1])
    elif temp[0] == 3:
        print(deq.popleft() if deq else -1)
    elif temp[0] == 4:
        print(deq.pop() if deq else -1)
    elif temp[0] == 5:
        print(len(deq))
    elif temp[0] == 6:
        print(0 if deq else 1)
    elif temp[0] == 7:
        print(deq[0] if deq else -1)
    elif temp[0] == 8:
        print(deq[-1] if deq else -1)

