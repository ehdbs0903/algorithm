import sys

input = sys.stdin.readline

n = int(input())

arr = []
ret = 0

def backtracking(len):
    global ret
    if len == n:
        ret += 1
    else:
        for i in range(n):
            if i not in arr:
                flag = 0
                for j in range(len):
                    if len - j == abs(i - arr[j]):
                        flag = 1
                        break
                if flag == 0:
                    arr.append(i)
                    backtracking(len + 1)
                    arr.pop()

backtracking(0)
print(ret)
