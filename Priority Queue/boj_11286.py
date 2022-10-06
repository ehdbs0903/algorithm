import sys
import heapq

input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        print(heapq.heappop(heap)[1] if heap else 0)

