import sys

input = sys.stdin.readline

n = int(input())

nums = [int(input()) for i in range(1, n+1)]
stack = []
op = []
flag = 0
i = 0
j = 1
while i < n:
    if j < nums[i]:
        stack.append(j)
        op.append("+")
        j += 1
    elif j == nums[i]:
        op.append("+")
        op.append("-")
        j += 1
        i += 1
    else:
        if stack[-1] != nums[i]:
            flag = 1
            break
        else:
            stack.pop()
            op.append("-")
            i += 1

if flag:
    print("NO")
else:
    for i in op:
        print(i)
