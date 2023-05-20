import sys
import math

input = sys.stdin.readline


def is_prime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    for _ in range(int(input())):
        n = int(input())

        while True:
            if is_prime(n):
                break
            n += 1

        print(n)


main()
