#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int bfs(const int& n, const int& m, vector<string>& board) {
	int dx[4] = { -1, 1, 0 ,0 };
	int dy[4] = { 0, 0, -1, 1 };
	vector<vector<vector<int>>> visited(n, vector<vector<int>>(m, vector<int>(2)));
	queue<vector<int>> q;

	q.push({ 0, 0, 0 });
	visited[0][0][0] = 1;

	while (!q.empty()) {
		int x, y, flag;

		x = q.front()[0];
		y = q.front()[1];
		flag = q.front()[2];
		q.pop();

		if (x == n - 1 && y == m - 1)
			return visited[x][y][flag];

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
				continue;

			if (board[nx][ny] == '0' && !visited[nx][ny][flag]) {
				visited[nx][ny][flag] = visited[x][y][flag] + 1;
				q.push({ nx, ny, flag });
			}
			else if (board[nx][ny] == '1' && !flag && !visited[nx][ny][1]) {
				visited[nx][ny][1] = visited[x][y][flag] + 1;
				q.push({ nx, ny, 1 });
			}
		}
	}

	return -1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m;

	cin >> n >> m;


	vector<string> board(n);

	for (int i = 0; i < n; i++) {
		cin >> board[i];
	}

	int result = bfs(n, m, board);
	cout << result;

	return 0;
}
