import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    try:
        s = input().rstrip()
        n = int(input())
        idx = 1
        nums = deque(input()[1:-2].split(','))
        if nums[0] == '':
            nums.pop()
        for ss in s:
            if ss == 'R':
                idx *= -1
            elif ss == 'D':
                if idx < 0:
                    nums.pop()
                else:
                    nums.popleft()
        if idx > 0:
            print("[" + ",".join(list(nums)) + "]")
        else:
            print("[" + ",".join(reversed(list(nums))) + "]")
    except:
        print("error")
