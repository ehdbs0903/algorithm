import sys

input = sys.stdin.readline


def dfs(v):
    for g in graph[v]:
        if visited[g] != ans:
            visited[g] = ans

            if not match[g] or dfs(match[g]):
                match[g] = v
                return True

    return False


n = int(input())
m = int(input())

board = [[0] * n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

left = [[0] * n for _ in range(n)]
right = [[0] * n for _ in range(n)]

cnt = 1
l = 0
for k in range(2 * n - 1):
    if k < n:
        i, j = 0, k
    else:
        i, j = k - n + 1, n - 1

    flag = False

    for _ in range(k + 1):
        if not (0 <= i < n and 0 <= j < n):
            break

        if not board[i][j]:
            left[i][j] = cnt
            l = cnt
            flag = True
        else:
            if flag:
                cnt += 1
                flag = False

        i += 1
        j -= 1

    if flag:
        cnt += 1
        flag = False

cnt = 1
r = 0
for k in range(2 * n - 1):
    if k < n:
        i, j = 0, n - k - 1
    else:
        i, j = k - n + 1, 0

    flag = False

    for _ in range(k + 1):
        if not (0 <= i < n and 0 <= j < n):
            break

        if not board[i][j]:
            right[i][j] = cnt
            r = cnt
            flag = True
        else:
            if flag:
                cnt += 1
                flag = False

        i += 1
        j += 1

    if flag:
        cnt += 1
        flag = False

graph = [[] for _ in range(l + 1)]
for i in range(n):
    for j in range(n):
        if not board[i][j]:
            graph[left[i][j]].append(right[i][j])

match = [0] * (r + 1)
visited = [-1] * (r + 1)
ans = 0

for i in range(1, l + 1):
    ans += dfs(i)

print(ans)

