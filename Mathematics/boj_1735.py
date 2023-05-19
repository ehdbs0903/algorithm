def gcd(a, b):
    while b:
        if a > b:
            a, b = b, a
        b %= a
    return a


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

numerator = (a1 * b2) + (a2 * b1)
denominator = b1 * b2

cd = gcd(numerator, denominator)
print(numerator // cd, denominator // cd)
