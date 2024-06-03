import sys

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]
    
arr.sort()

for i in arr:
    print(i)
