n = int(input())
facto = list(map(int, input().split()))

count = [[0] * 3 for _ in range(n)]

count[0][0] = facto[0]
facto[0] = 0

for i in range(n - 1):
    count[i][0] += facto[i]
    facto[i] = 0

    if facto[i+1] > count[i][0]:
        count[i+1][1] += count[i][0]
        facto[i+1] -= count[i][0]
    else:
        count[i+1][1] += facto[i+1]
        facto[i+1] -= count[i+1][1]

    if facto[i+1] > count[i][1]:
        count[i+1][2] += count[i][1]
        facto[i+1] -= count[i][1]
    else:
        count[i+1][2] += facto[i+1]
        facto[i+1] -= count[i+1][2]

count[n-1][0] = facto[n-1]

ans = 0
for i in range(n):
    for j in range(3):
        if j == 0:
            ans += count[i][j] * 3
        else:
            ans += count[i][j] * 2

print(ans)
