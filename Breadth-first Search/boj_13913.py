from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for nx in (x * 2, x - 1, x + 1):
            if 0 <= nx <= 100000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)
                if nx == k:
                    return visited[k]
    return 0


n, k = map(int, input().split())
visited = [-1] * 100001
visited[n] = 0
cnt = bfs(n) - 1
print(cnt + 1)
li = deque()
while cnt > -1:
    if k % 2 == 0 and visited[k // 2] == cnt:
        li.appendleft(k)
        k //= 2
    elif visited[k + 1] == cnt:
        li.appendleft(k)
        k += 1
    elif visited[k - 1] == cnt:
        li.appendleft(k)
        k -= 1

    cnt -= 1

li.appendleft(n)
print(*li)

