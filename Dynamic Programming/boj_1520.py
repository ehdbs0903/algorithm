import sys

input = sys.stdin.readline
sys.setrecursionlimit(250000)


def main():
    n, m = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        if x == n - 1 and y == m - 1:
            return 1

        if visited[x][y] != -1:
            return visited[x][y]

        cases = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] < board[x][y]:
                    cases += dfs(nx, ny)

        visited[x][y] = cases
        return visited[x][y]

    print(dfs(0, 0))


if __name__ == "__main__":
    main()
