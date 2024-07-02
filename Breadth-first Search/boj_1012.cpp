#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void bfs(const int& n, const int& m, int x, int y, vector<vector<int>>& board, vector<vector<int>>& visited) {
	int dx[4] = { -1, 1, 0, 0 };
	int dy[4] = { 0, 0, -1, 1 };
	
	queue<pair<int, int>> q;
	int nx, ny;

	visited[x][y] = 1;
	q.push({ x, y });


	while (!q.empty()) {
		x = q.front().first;
		y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			nx = x + dx[i];
			ny = y + dy[i];

			if (nx >= 0 && nx < n && ny >= 0 && ny < m &&
				board[nx][ny] && !visited[nx][ny]) {
				visited[nx][ny] = 1;
				
				q.push({ nx, ny });
			}
		}
	}
}

int main() {
	int t;

	cin >> t;

	while (t--) {
		int m, n, k, cnt = 0;

		cin >> m >> n >> k;

		vector<vector<int>> board(n, vector<int>(m, 0));
		vector<vector<int>> visited(n, vector<int>(m, 0));
		
		while (k--) {
			int x, y;

			cin >> y >> x;

			board[x][y] = 1;
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (board[i][j] && !visited[i][j]) {
					bfs(n, m, i, j, board, visited);
					cnt += 1;
				}
			}
		}

		cout << cnt << "\n";
	}

	return 0;
}
