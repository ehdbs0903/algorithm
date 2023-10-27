from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))

ans = []
while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)
    
    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(*ans)

