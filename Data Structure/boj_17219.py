import sys

input = sys.stdin.readline

n, m = map(int, input().split())

passwords = dict()

for _ in range(n):
    site, pwd = input().rstrip().split()
    passwords[site] = pwd

for _ in range(m):
    site = input().rstrip()
    print(passwords[site])
