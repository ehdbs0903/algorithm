#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int board[25][25];
int visited[25][25] = {};

int bfs(int x, int y, int n) {
	int dx[4] = { -1, 1, 0, 0 };
	int dy[4] = { 0, 0, -1, 1 };
	queue<pair<int, int>> q;
	int cnt = 1;

	q.push(make_pair(x, y));
	visited[x][y] = 1;

	while (!q.empty()) {
		x = q.front().first, y = q.front().second;
		q.pop();

		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k], ny = y + dy[k];

			if (nx < 0 || nx >= n || ny < 0 || ny >= n)
				continue;
			if (!board[nx][ny] || visited[nx][ny])
				continue;

			visited[nx][ny] = 1;
			q.push(make_pair(nx, ny));
			cnt++;
		}
	}

	return cnt;
}

int main() {
	int n;

	cin >> n;

	for (int i = 0; i < n; i++) {
		string line;
		cin >> line;
		
		for (int j = 0; j < n; j++) {
			board[i][j] = line[j] - '0';
		}
	}

	int cnt = 0;
	vector<int> ans;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (board[i][j] && !visited[i][j]) {
				ans.emplace_back(bfs(i, j, n));
				cnt++;
			}
		}
	}

	sort(ans.begin(), ans.end());

	cout << cnt << "\n";
	for (auto a : ans)
		cout << a << "\n";

	return 0;
}
