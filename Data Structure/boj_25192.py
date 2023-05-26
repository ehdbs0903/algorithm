import sys

input = sys.stdin.readline


def main():
    n = int(input())

    name_set = set()
    cnt = 0

    for _ in range(n):
        s = input()
        if s != "ENTER\n":
            name_set.add(s)
        else:
            cnt += len(name_set)
            name_set = set()

    cnt += len(name_set)

    print(cnt)


main()