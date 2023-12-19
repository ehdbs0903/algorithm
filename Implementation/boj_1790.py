n, k = map(int, input().split())

new_num_len = 0
for i in range(1, n+1):
    new_num_len += len(str(i))
    if new_num_len >= k:
        new_num_len -= len(str(i))
        print(str(i)[k - new_num_len - 1])
        break

else:
    print(-1)

