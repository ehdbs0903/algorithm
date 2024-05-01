from itertools import permutations

N, M = map(int, input().split())
numlist = list(map(int, input().split()))
case = sorted(set(permutations(numlist, M)))

for i in case:
    for j in i:
        print(j, end=" ")
    print()
