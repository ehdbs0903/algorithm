string = input()

stack = []

try:
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)

        elif s == ')' or s == ']':
            temp = 0
            while isinstance(stack[-1], int):
                temp += stack.pop()

            if not temp:
                temp = 1

            stack.pop()

            if s == ')' and stack[-1] == '(':
                stack.append(temp * 2)

            elif s == ']' and stack[-1] == '[':
                stack.append(temp * 3)

    print(sum(stack))

except:
    print(0)
