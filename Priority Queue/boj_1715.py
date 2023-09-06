import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]

heapq.heapify(cards)

ans = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    temp = a + b

    heapq.heappush(cards, temp)
    ans += temp

print(ans)

