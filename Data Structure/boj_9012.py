n = int(input())

for _ in range(n):
    s = input()
    stk = []
    is_valid = True
    for char in s:
        if char == '(':
            stk.append(char)
        elif char == ')':
            if not stk or stk[-1] != '(':
                is_valid = False
                break
            stk.pop()
    if is_valid and not stk:
        print('YES')
    else:
        print('NO')
