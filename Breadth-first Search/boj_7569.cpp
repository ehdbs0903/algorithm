#include <iostream>
#include <queue>
#include <tuple>
using namespace std;

int board[100][100][100];
int visited[100][100][100] = {};

void bfs(int n, int m, int h) {
    int dx[6] = {-1, 1, 0, 0, 0, 0};
    int dy[6] = {0, 0, -1, 1, 0, 0};
    int dz[6] = {0, 0, 0, 0, -1, 1};

    queue<tuple<int, int, int>> q;

    for (int k = 0; k < h; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[k][i][j] == 1) {
                    q.push(make_tuple(k, i, j));
                    visited[k][i][j] = 1;
                }
            }
        }
    }

    while (!q.empty()) {
        int z, x, y;
        tie(z, x, y) = q.front();
        q.pop();

        for (int i = 0; i < 6; i++) {
            int nz = z + dz[i];
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nz < 0 || nz >= h || nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;

            if (board[nz][nx][ny] != 0 || visited[nz][nx][ny] != 0)
                continue;

            visited[nz][nx][ny] = visited[z][x][y] + 1;
            board[nz][nx][ny] = 1;
            q.push(make_tuple(nz, nx, ny));
        }
    }
}

int main() {
    int n, m, h;

    cin >> m >> n >> h;

    for (int k = 0; k < h; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> board[k][i][j];
            }
        }
    }

    bfs(n, m, h);

    int cnt = 0;

    for (int k = 0; k < h; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cnt = max(cnt, visited[k][i][j]);

                if (board[k][i][j] == 0) {
                    cout << -1;
                    return 0;
                }
            }
        }
    }

    cout << cnt - 1;

    return 0;
}
