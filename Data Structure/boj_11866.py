from collections import deque


def josephus(N, K):
    q = deque(range(1, N + 1))
    result = []
    
    while q:
        q.rotate(-(K-1))
        result.append(q.popleft())
    return result


N, K = map(int, input().split())

ans = josephus(N, K)

print("<" + ", ".join(map(str, ans)) + ">")
