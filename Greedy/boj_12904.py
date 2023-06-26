s1 = list(input())
s2 = list(input())

ans = 0
while s2:
    if s2[-1] == 'A':
        s2.pop()
    elif s2[-1] == 'B':
        s2.pop()
        s2.reverse()
    if s1 == s2:
        ans = 1
        break

print(ans)
