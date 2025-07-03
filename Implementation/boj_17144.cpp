#include <iostream>

using namespace std;

int r, c, t;
int board[50][50];
int temp_board[50][50];
int top_purifier = -1, bottom_purifier = -1;

void spread() {
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            temp_board[i][j] = 0;

    const int dx[4] = { -1, 1, 0, 0 };
    const int dy[4] = { 0, 0, -1, 1 };

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (board[i][j] > 0) {
                int spread_amount = board[i][j] / 5;
                int cnt = 0;

                for (int d = 0; d < 4; d++) {
                    int ni = i + dx[d], nj = j + dy[d];

                    if (ni < 0 || ni >= r || nj < 0 || nj >= c)
                        continue;

                    if (board[ni][nj] == -1)
                        continue;

                    temp_board[ni][nj] += spread_amount;
                    cnt++;
                }
                board[i][j] -= spread_amount * cnt;
            }
        }
    }

    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            board[i][j] += temp_board[i][j];
}

void clean() {
    int t = top_purifier;

    for (int i = t - 1; i > 0; i--) board[i][0] = board[i - 1][0];
    for (int j = 0; j < c - 1; j++) board[0][j] = board[0][j + 1];
    for (int i = 0; i < t; i++) board[i][c - 1] = board[i + 1][c - 1];
    for (int j = c - 1; j > 1; j--) board[t][j] = board[t][j - 1];
    board[t][1] = 0;

    int b = bottom_purifier;

    for (int i = b + 1; i < r - 1; i++) board[i][0] = board[i + 1][0];
    for (int j = 0; j < c - 1; j++) board[r - 1][j] = board[r - 1][j + 1];
    for (int i = r - 1; i > b; i--) board[i][c - 1] = board[i - 1][c - 1];
    for (int j = c - 1; j > 1; j--) board[b][j] = board[b][j - 1];
    board[b][1] = 0;

    board[t][0] = board[b][0] = -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> r >> c >> t;

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> board[i][j];

            if (board[i][j] == -1) {
                if (top_purifier == -1)
                    top_purifier = i;
                else
                    bottom_purifier = i;
            }
        }
    }

    while (t--) {
        spread();
        clean();
    }

    int answer = 0;

    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            if (board[i][j] > 0)
                answer += board[i][j];

    cout << answer;

    return 0;
}
