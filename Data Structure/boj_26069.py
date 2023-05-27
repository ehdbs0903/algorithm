import sys
input = sys.stdin.readline

dance_set = {'ChongChong'}

for i in range(int(input())):
    a, b = input().split()

    if a in dance_set or b in dance_set:
        dance_set.add(b)
        dance_set.add(a)

print(len(dance_set))
