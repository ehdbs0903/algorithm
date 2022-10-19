n = int(input())

is_prime = [False] * 2 + [True] * (n - 1)
prime = []

for i in range(2, n + 1):
    if is_prime[i]:
        prime.append(i)
        is_prime[i * 2:: i] = [False] * (n // i - 1)

left = right = 0
cnt = 0
temp_sum = 0
l = len(prime)

while True:
    if temp_sum == n:
        cnt += 1
        temp_sum -= prime[left]
        left += 1
    elif temp_sum > n:
        temp_sum -= prime[left]
        left += 1
    elif right == l:
        break
    else:
        temp_sum += prime[right]
        right += 1

print(cnt)

