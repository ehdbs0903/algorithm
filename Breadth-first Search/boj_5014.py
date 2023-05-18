from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)

q = deque()
q.append(s)
visited[s] = 1
while q:
    x = q.popleft()
    for nx in (x + u, x - d):
        if 0 < nx <= f and not visited[nx]:
            q.append(nx)
            visited[nx] = visited[x] + 1

if visited[g]:
    print(visited[g] - 1)
else:
    print("use the stairs")

