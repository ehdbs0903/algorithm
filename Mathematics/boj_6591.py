while True:
    n, k = map(int, input().split())

    if n == 0 and k == 0:
        break

    numerator = 1
    denominator = 1

    for i in range(n, max(k, n-k), -1):
        numerator *= i
    for i in range(1, min(n-k, k) + 1):
        denominator *= i

    print(numerator // denominator)
