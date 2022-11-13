import sys

input = sys.stdin.readline


def dfs(v):
    for g in graph[v]:
        if visited[g] != cnt:
            visited[g] = cnt

            if match[g] == -1 or dfs(match[g]):
                match[g] = v
                return True

    return False


n = int(input())
arr = list(map(int, input().split()))

prime = [False, False] + [True for i in range(1999)]
for i in range(2, 45):
    if prime[i]:
        for j in range(i * 2, 2001, i):
            prime[j] = False

odd = []
even = []

for a in arr:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)

if arr[0] % 2 == 0:
    A = even
    B = odd
else:
    B = even
    A = odd

k = len(A)
if k != n // 2:
    print(-1)
    exit()

graph = [[] for _ in range(k)]
for i in range(k):
    for j in range(k):
        if prime[A[i] + B[j]]:
            graph[i].append(j)

match = [-1] * k
visited = [-1] * k
ans = []

for a in graph[0]:
    match = [-1] * k
    visited = [-1] * k

    match[a] = 0
    cnt = 0

    for j in range(1, k):
        visited[a] = cnt
        cnt += dfs(j)

    if cnt == k - 1:
        ans.append(B[a])

if ans:
    ans.sort()
    print(*ans)

else:
    print(-1)

