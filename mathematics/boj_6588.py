import sys
import math

input = sys.stdin.readline

def isPrime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return 0
    return 1

while True:
    n = int(input())

    if n == 0:
        break

    a = 3
    b = n - 3

    while a < n // 2:
        if isPrime(a) == 1 and isPrime(b) == 1:
            break
        else:
            a += 2
            b -= 2

    if a != 1:
        print("{0} = {1} + {2}".format(n, a, b))
    else:
        print("Goldbach's conjecture is wrong.")
