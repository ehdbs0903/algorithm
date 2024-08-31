#include <iostream>
#include <queue>
using namespace std;

int n;
int board[100][100];

void bfs(int x) {
	queue<int> q;
	int visited[100] = {};

	q.push(x);

	while (!q.empty()) {
		int cx = q.front();
		q.pop();

		for (int nx = 0; nx < n; nx++) {
			if (board[cx][nx] && !visited[nx]) {
				q.push(nx);
				visited[nx] = 1;
				board[x][nx] = 1;
			}
		}
	}
}

int main() {
	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> board[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		bfs(i);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << board[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}
