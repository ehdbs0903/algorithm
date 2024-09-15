#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int bfs(int x, int y, int n, int m, const vector<string> board) {
    int dx[] = { -1 ,1 ,0 ,0 };
    int dy[] = { 0, 0, -1, 1 };
    
    queue<pair<int, int>> q;
    vector<vector<int>> visited(n, vector<int>(m));
    int cnt = 0;

    q.push(make_pair(x, y));
    visited[x][y] = 1;
    
    while (!q.empty()) {
        x = q.front().first;
        y = q.front().second;
        q.pop();

        if (board[x][y] == 'P')
            cnt++;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 > nx || nx >= n || 0 > ny || ny >= m)
                continue;

            if (board[nx][ny] != 'X' && !visited[nx][ny]) {
                q.push(make_pair(nx, ny));
                visited[nx][ny] = 1;
            }
        }
    }

    return cnt;
}

int main() {
    int n, m;

    cin >> n >> m;

    vector<string> board(n);

    int sx = -1, sy = -1;

    for (int i = 0; i < n; i++) {
        cin >> board[i];

        for (int j = 0; j < m; j++) {
            if (board[i][j] == 'I') {
                sx = i;
                sy = j;
            }
        }
    }

    int ret = bfs(sx, sy, n, m, board);

    if (ret)
        cout << ret;
    else
        cout << "TT";

    return 0;
}
