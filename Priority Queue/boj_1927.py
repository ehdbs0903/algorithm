import sys
import heapq

input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(heap, x)
    else:
        print(heapq.heappop(heap) if heap else 0)

