#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void bfs(int r, int c, int n, int m, vector<vector<int>>& graph) {
    int dx[] = { -1 ,1, 0, 0 };
    int dy[] = { 0, 0, -1, 1 };

    queue<pair<int, int>> q;
    q.push({ r, c });
    graph[r][c] = 1;

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        if (x == n - 1 && y == m - 1)
            return;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;

            if (graph[nx][ny] != 0)
                continue;

            q.push({ nx, ny });
            graph[nx][ny] = graph[x][y] + 1;
        }
    }

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;

    cin >> n >> m >> k;

    vector<vector<int>> graph(n, vector<int>(m));

    while (k--) {
        int r, c, d;

        cin >> r >> c >> d;

        r--;
        c--;

        for (int dx = -d; dx <= d; ++dx) {
            int dy = d - abs(dx);

            int x1 = r + dx, y1 = c + dy;
            if (0 <= x1 && x1 < n && 0 <= y1 && y1 < m)
                graph[x1][y1] = -1;

            int x2 = r + dx, y2 = c - dy;
            if (0 <= x2 && x2 < n && 0 <= y2 && y2 < m)
                graph[x2][y2] = -1;
        }
    }

    bfs(0, 0, n, m, graph);

    int ans = graph[n - 1][m - 1] - 1;

    if (ans > 0)
        cout << "YES\n" << ans;
    else
        cout << "NO";

    return 0;
}
