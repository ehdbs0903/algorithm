import math

prime = []

for i in range(2, 10000):
    flag = 0
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            flag = 1
    if flag == 0:
        prime.append(i)

t = int(input())

for _ in range(t):
    n = int(input())
    left = n // 2
    right = left
		
    while True:
        if left in prime and right in prime:
            print(left, right)
            break
        left -= 1
        right += 1
