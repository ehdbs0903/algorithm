def gcd(a, b):
    while b:
        if a > b:
            a, b = b, a
        b %= a
    return a


a, b = map(int, input().split())

print(a * b//gcd(a, b))
