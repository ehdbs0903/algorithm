arr = set(range(1, 10001))

for i in range(1, 10001) :
    for j in str(i) :
        i += int(j)
    arr.discard(i)

for i in arr :
    print(i)
