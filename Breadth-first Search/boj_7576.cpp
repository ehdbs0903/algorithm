#include <iostream>
#include <queue>
#include <tuple>
using namespace std;

int main() {
    int m, n;

    cin >> m >> n;

    int board[1000][1000];
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }

    int dx[4] = { -1, 1, 0, 0 };
    int dy[4] = { 0, 0, -1, 1 };
    int x, y;
    queue<pair<int, int>> q;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 1)
                q.push(make_pair(i, j));
        }
    }

    while (!q.empty()) {
        tie(x, y) = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;

            if (board[nx][ny] == 0) {
                q.push(make_pair(nx, ny));
                board[nx][ny] = board[x][y] + 1;
            }
        }
    }

    int days = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 0) {
                cout << -1;
                return 0;
            }
            days = max(days, board[i][j]);
        }
    }

    cout << days - 1;

    return 0;
}
