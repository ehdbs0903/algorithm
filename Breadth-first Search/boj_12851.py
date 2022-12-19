from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0
    cnt[x] = 1
    while q:
        x = q.popleft()
        for nx in (x * 2, x - 1, x + 1):
            if 0 <= nx <= 100000:
                if visited[nx] == -1:
                    visited[nx] = visited[x] + 1
                    cnt[nx] = cnt[x]
                    q.append(nx)
                else:
                    if visited[nx] == visited[x] + 1:
                        cnt[nx] += cnt[x]


n, k = map(int, input().split())
visited = [-1] * 100001
cnt = [0] * 100001
bfs(n)
print(visited[k])
print(cnt[k])

