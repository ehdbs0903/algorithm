import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

def backtracking():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
    else:
        for j in range(1, n + 1):
            if j not in arr:
                arr.append(j)
                backtracking()
                arr.pop()

backtracking()