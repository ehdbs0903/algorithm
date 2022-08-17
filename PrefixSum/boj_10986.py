n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))

temp = 0
sums_mod = [0 for i in range(m)]
for i in range(n + 1):
    temp += nums[i]
    sums_mod[temp % m] += 1

cnt = 0
for i in sums_mod:
    cnt += i*(i-1)//2
print(cnt)
