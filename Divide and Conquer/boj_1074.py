def recursion(n, x, y):
    global ans

    if n == 0:
        ans += x * 2 + y
        print(ans)
        return

    if x < 2 ** n and y < 2 ** n:
        recursion(n - 1, x, y)

    elif x < 2 ** n and y >= 2 ** n:
        ans += 2 ** (2 * n)
        recursion(n - 1, x, y - 2 ** n)

    elif x >= 2 ** n and y < 2 ** n:
        ans += 2 * 2 ** (2 * n)
        recursion(n - 1, x - 2 ** n, y)


    else:
        ans += 3 * 2 ** (2 * n)
        recursion(n - 1, x - 2 ** n, y - 2 ** n)


N, r, c = map(int, input().split())

ans = 0
recursion(N - 1, r, c)

