s = ""

def solution(x, y, n):
    global s
    check = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != board[i][j]:
                check = -1
                break

    if check == -1:
        s = s + "("
        n = n // 2
        solution(x, y, n)
        solution(x, y + n, n)
        solution(x + n, y, n)
        solution(x + n, y + n, n)
        s = s + ")"

    elif check == "1":
        s = s + "1"
    else:
        s = s + "0"


n = int(input())

board = []
for _ in range(n):
  board.append(input())

solution(0,0,n)
print(s)
