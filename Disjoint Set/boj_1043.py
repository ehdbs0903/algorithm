import sys

input = sys.stdin.readline

n, m = map(int, input().split())
knowing = set(input().split()[1:])
parties = [set(input().split()[1:]) for _ in range(m)]

for _ in range(m):
    for party in parties:
        if party & knowing:
            knowing = knowing.union(party)

cnt = 0
for party in parties:
    if party & knowing:
        continue
    cnt += 1

print(cnt)
