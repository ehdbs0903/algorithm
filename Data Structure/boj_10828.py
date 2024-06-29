import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    cmd = input().rstrip()
    if cmd[:4] == "push":
        cmd, i = cmd.split()
        arr.append(i)
    elif cmd == "pop":
        if len(arr):
            print(arr.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(arr))
    elif cmd ==  "empty":
        if len(arr):
            print(0)
        else:
            print(1)
    elif cmd == "top":
        if len(arr):
            print(arr[-1])
        else:
            print(-1)
