import sys

input = sys.stdin.readline

m = int(input())

s = set()
for _ in range(m):
    temp = input().rstrip()
    op = temp[:2]
    if op == "ad":
        x = int(temp[-2:])
        s.add(x)

    elif op == "re":
        x = int(temp[-2:])
        if x in s:
            s.remove(x)

    elif op == "ch":
        x = int(temp[-2:])
        if x in s:
            print(1)
        else:
            print(0)

    elif op == "to":
        x = int(temp[-2:])
        if x in s:
            s.remove(x)
        else:
            s.add(x)

    elif op == "al":
        s = set([i for i in range(1, 21)])

    else:
        s = set()
