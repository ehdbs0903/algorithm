import sys

input = sys.stdin.readline


def backtracking(x, y, cnt):
    global alphabets

    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            next_char_mask = ord(board[nx][ny]) - ord('A')

            if alphabets & (1 << next_char_mask) == 0:
                alphabets = alphabets | (1 << next_char_mask)
                backtracking(nx, ny, cnt + 1)
                alphabets = alphabets & ~(1 << next_char_mask)


r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


alphabets = 1 << ord(board[0][0]) - ord('A')

ans = 0
backtracking(0, 0, 1)

print(ans)
