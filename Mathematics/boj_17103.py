def main():
    sieve = [1] * 1000000
    prime = []

    for i in range(2, 1000000):
        if sieve[i]:
            prime.append(i)
            for j in range(2 * i, 1000000, i):
                sieve[j] = 0

    for _ in range(int(input())):
        n = int(input())

        ans = 0
        for p in prime:
            if p > n // 2:
                break

            if sieve[n - p]:
                ans += 1

        print(ans)


main()