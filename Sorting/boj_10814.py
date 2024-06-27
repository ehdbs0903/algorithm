n = int(input())

people = []
for _ in range(n):
    people.append(tuple(input().split()))

people.sort(key = lambda x: int(x[0]))

for i in people:
    print(i[0], i[1])
