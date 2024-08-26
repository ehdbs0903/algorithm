#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

char graph[100][100] = {};
int visited[100][100] = {};
int dx[] = { -1, 1, 0, 0 };
int dy[] = { 0, 0, -1, 1 };

void bfs(int x, int y, int n) {
    queue<pair<int, int>> q;
    char color = graph[x][y];

    q.push({ x, y });
    visited[x][y] = 1;

    while (!q.empty()) {
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        for (int k = 0; k < 4; ++k) {
            int nx = cx + dx[k];
            int ny = cy + dy[k];

            if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                if (visited[nx][ny] == 0 && graph[nx][ny] == color) {
                    visited[nx][ny] = 1;
                    q.push({ nx, ny });
                }
            }
        }
    }
}

int main() {
    int n;

    cin >> n;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> graph[i][j];
        }
    }

    int cnt1 = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (visited[i][j] == 0) {
                bfs(i, j, n);
                cnt1++;
            }

            if (graph[i][j] == 'G') {
                graph[i][j] = 'R';
            }
        }
    }

    fill(&visited[0][0], &visited[0][0] + 100 * 100, 0);

    int cnt2 = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (visited[i][j] == 0) {
                bfs(i, j, n);
                cnt2++;
            }
        }
    }

    cout << cnt1 << " " << cnt2 << endl;

    return 0;
}
