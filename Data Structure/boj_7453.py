import sys

input = sys.stdin.readline

number = int(input())
a_list, b_list, c_list, d_list = [], [], [], []

for _ in range(number):
    a, b, c, d = map(int, input().split())
    a_list.append(a); b_list.append(b); c_list.append(c); d_list.append(d)

dic = dict()
for a in a_list:
    for b in b_list:
        dic[a+b] = dic.get(a + b, 0) + 1

cnt = 0
for c in c_list:
    for d in d_list:
        cnt += dic.get(-(c + d),0)

print(cnt)
