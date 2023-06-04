def factorial(a):
    ret = 1
    for i in range(1, a+1):
        ret = (ret * i) % p

    return ret


def multi(a, n):
    if n == 1:
        return a % p
    else:
        temp = multi(a, n // 2)
        if n % 2:
            return (temp * temp * a) % p
        else:
            return (temp * temp) % p


n, k = map(int, input().split())
p = 1000000007

print(factorial(n) * multi(factorial(n-k) * factorial(k), p-2) % p)

