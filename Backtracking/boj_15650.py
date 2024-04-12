import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0]

def backtracking():
    if len(arr) == m+1:
        print(' '.join(map(str, arr[1:])))
    else:
        for i in range(1, n + 1):
            if i > arr[-1]:
                arr.append(i)
                backtracking()
                arr.pop()

backtracking()
