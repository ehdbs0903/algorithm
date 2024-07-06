import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dic[a] = str(i)
    dic[str(i)] = a

# 'm'개의 쿼리를 처리하는 루프
for _ in range(m):
    temp = input().rstrip()
    print(dic[temp])
