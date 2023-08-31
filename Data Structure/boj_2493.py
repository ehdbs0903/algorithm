n = int(input())
tower = list(map(int, input().split()))

stack = []
ans = [0] * n
for i in range(n-1, -1, -1):
    if stack and tower[stack[-1]] < tower[i]:
        while stack and tower[stack[-1]] < tower[i]:
            ans[stack.pop()] = i + 1
    stack.append(i)

print(*ans)

