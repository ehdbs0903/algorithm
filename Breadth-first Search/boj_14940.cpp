#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
using namespace std;

int board[1000][1000];

void bfs(int x, int y, int n, int m) {
	int dx[] = { -1, 1, 0, 0 };
	int dy[] = { 0, 0, -1, 1 };
	vector<vector<int>> visited(n, vector<int>(m));
	queue<pair<int, int>> q;

	q.push(make_pair(x, y));
	visited[x][y] = 1;
	board[x][y] = 0;

	while (!q.empty()) {
		tie(x, y) = q.front();
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;

			if (board[nx][ny] == 1 && !visited[nx][ny]) {
				q.push(make_pair(nx, ny));
				visited[nx][ny] = 1;
				board[nx][ny] = board[x][y] + 1;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (board[i][j] == 1 && !visited[i][j]) {
				board[i][j] = -1;
			}
		}
	}
}

int main() {
	int n, m;
	cin >> n >> m;

	int x, y;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> board[i][j];
			if (board[i][j] == 2) {
				x = i;
				y = j;
			}
		}
	}

	bfs(x, y, n, m);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << board[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}
