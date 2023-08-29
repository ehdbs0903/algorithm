import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

cost = [[10000001] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                cost[i][j] = 0
            else:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for row in cost[1:]:
    for col in row[1:]:
        if col == 10000001:
            print(0, end=' ')
        else:
            print(col, end=' ')
    print()
