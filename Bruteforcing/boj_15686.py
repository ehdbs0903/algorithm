import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

houses = []
chicken_houses = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            houses.append([i, j])
        elif board[i][j] == 2:
            chicken_houses.append([i, j])

ans = 1e9

for combination in combinations(chicken_houses, m):
    chicken_distance = 0

    for h_x, h_y in houses:
        temp = 1e9

        for comb in combination:
            temp = min(temp, abs(h_x - comb[0]) + abs(h_y - comb[1]))

        chicken_distance += temp

    ans = min(ans, chicken_distance)

print(ans)

