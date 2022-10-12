import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    min_heap = []
    max_heap = []
    visited = {}
    for _ in range(int(input())):
        op, n = input().split()
        n = int(n)
        if op == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            try:
                visited[n] += 1
            except:
                visited[n] = 1

        elif op == 'D':
            if n == 1:
                while max_heap and not visited[-max_heap[0]]:
                    heapq.heappop(max_heap)

                if max_heap:
                    visited[-heapq.heappop(max_heap)] -= 1
            elif n == -1:
                while min_heap and not visited[min_heap[0]]:
                    heapq.heappop(min_heap)

                if min_heap:
                    visited[heapq.heappop(min_heap)] -=1

    while max_heap and not visited[-max_heap[0]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0]]:
        heapq.heappop(min_heap)

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")

