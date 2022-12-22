n = int(input())

bg = 0
while n >= 0:
    if n % 5 == 0:
        bg += n // 5
        print(bg)
        break
    n -= 3
    bg += 1
else:
    print(-1)
