n = int(input())

def factorial(a):
    num = 1
    for i in range(2, a+1):
        num *= i
    return num

cnt = 0

arr = str(factorial(n))

for i in list(reversed(arr)):
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)
