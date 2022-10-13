import sys

input = sys.stdin.readline


def find(x):
    if x != vlist[x]:
        vlist[x] = find(vlist[x])
    return vlist[x]


v, e = map(int, input().split())
elist = [[*map(int, input().split())] for _ in range(e)]
vlist = [i for i in range(v + 1)]

elist.sort(key=lambda x: x[2])

ans = 0
for a, b, c in elist:
    v1, v2 = find(a), find(b)

    if v1 != v2:
        if v1 > v2:
            vlist[v1] = v2
        else:
            vlist[v2] = v1
        ans += c

print(ans)

