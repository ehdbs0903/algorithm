n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = int(input())
C = list(map(int, input().split()))

ret = []
for i in range(n-1, -1, -1):
    if A[i]:
        continue

    ret.append(B[i])

ret += C

print(*ret[:m])

