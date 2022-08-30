import math

m = 123456
arr = [0 for _ in range(m * 2 + 1)]

for i in range(2, m * 2 + 1):
	if i == 1:
		continue
	flag = 0
	for j in range(2, int(math.sqrt(i)) + 1):
		if i % j == 0:
			flag = 1
			break
	if flag == 0:
		arr[i] = 1

while True:
	n = int(input())
	if n == 0:
		break
	cnt = 0
	for i in range(n + 1, n * 2 + 1):
		if arr[i] == 1:
			cnt += 1
	print(cnt)
