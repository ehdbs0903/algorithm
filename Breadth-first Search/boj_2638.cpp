#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
	int n, m;

	cin >> n >> m;

	vector<vector<int>> board(n, vector<int>(m));

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> board[i][j];
		}
	}

	int time = 0;

	while (true)
	{
		int dx[4] = { -1, 1, 0, 0 };
		int dy[4] = { 0, 0, -1, 1 };

		vector<vector<int>> airCnt(n, vector<int>(m));
		vector<vector<int>> visited(n, vector<int>(m));
		queue<pair<int, int>> q;

		q.push(make_pair(0, 0));
		visited[0][0] = 1;

		while (!q.empty()) {
			auto cur = q.front();
			q.pop();

			int x = cur.first;
			int y = cur.second;

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx < 0 || nx >= n || ny < 0 || ny >= m)
					continue;

				if (board[nx][ny] == 0 && !visited[nx][ny]) {
					q.push(make_pair(nx, ny));
					visited[nx][ny] = 1;
				}
				else {
					airCnt[nx][ny]++;
				}
			}
		}

		vector<pair<int, int>> melt;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (board[i][j] && airCnt[i][j] >= 2) {
					melt.push_back(make_pair(i, j));
				}
			}
		}

		if (melt.empty())
			break;

		for (auto p : melt) {
			int x = p.first;
			int y = p.second;

			board[x][y] = 0;
		}

		time++;
	}
	
	cout << time;

	return 0;
}
