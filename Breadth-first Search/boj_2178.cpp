#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<string> board;

void bfs(int n, int m) {
	int x = 0, y = 0;
	queue<pair<int, int>> q;
	vector<vector<int>> visited(n, vector<int>(m));
	int dx[4] = { -1, 1, 0, 0 };
	int dy[4] = { 0, 0, -1, 1 };

	q.push({ x, y });
	visited[x][y] = 1;

	while (!q.empty()) {
		x = q.front().first;
		y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx >= 0 && nx < n && ny >= 0 && ny < m &&
				board[nx][ny] == '1' && !visited[nx][ny]) {
				q.push({ nx, ny });
				visited[nx][ny] = visited[x][y] + 1;
			}
		}
	}

	cout << visited[n - 1][m - 1];
}

int main() {
	int n, m;

	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		string temp;

		cin >> temp;

		board.emplace_back(temp);
	}

	bfs(n, m);

	return 0;
}
