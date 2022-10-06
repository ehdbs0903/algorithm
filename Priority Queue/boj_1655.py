import heapq
import sys

input = sys.stdin.readline

leftHeap = []
rightHeap = []
for i in range(int(input())):
    n = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -n)
    else:
        heapq.heappush(rightHeap, n)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        heapq.heappush(leftHeap, -heapq.heappop(rightHeap))
        heapq.heappush(rightHeap, -heapq.heappop(leftHeap))

    print(-leftHeap[0])
    
