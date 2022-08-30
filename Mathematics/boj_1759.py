from itertools import combinations

l, c = map(int, input().split())
s = list(map(str, input().split()))
s.sort()
for i in combinations(s, l):
    a = 0
    b = 0
    for j in i:
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            a += 1
        else:
            b += 1
        if a >= 1 and b >= 2:
            for k in i:
                print(k, end='')
            print()
            break
