import sys

input = sys.stdin.readline

n, h = map(int, input().split())

obstacles = [0] * h

for i in range(n):
    height = int(input())

    if i % 2:
        obstacles[h - height] += 1
    else:
        obstacles[0] += 1
        obstacles[height] -= 1

for i in range(1, h):
    obstacles[i] += obstacles[i - 1]

obstacle_min = min(obstacles)
print(obstacle_min, obstacles.count(obstacle_min))
