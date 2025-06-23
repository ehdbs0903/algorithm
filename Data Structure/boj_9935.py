s = input()
bomb = input()

lastChar = bomb[-1]
stack = []
length = len(bomb)

for char in s:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)
