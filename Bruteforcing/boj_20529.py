import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    mbti = list(map(str, input().rstrip().split()))
    
    if n > 32:
        print(0)
    else:
        distance = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                dist = 0
                for k in range(4):
                    if mbti[i][k] != mbti[j][k]:
                        dist += 1
                distance[i][j] = distance[j][i] = dist
    
        ans = 10
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    ans = min(ans, distance[i][j] + distance[j][k] + distance[k][i])

        print(ans)
