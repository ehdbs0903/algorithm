#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int MAX = 100001;

void bfs(int n, int k) {
	vector<int> visited(MAX, -1);
	queue<int> q;

	q.push(n);
	visited[n] = 0;

	while (!q.empty()) {
		int v = q.front();
		q.pop();

		if (v == k) {
			cout << visited[v];
			return;
		}

		for (int nv : {v - 1, v + 1, v * 2}) {
			if (nv >= 0 && nv < MAX && visited[nv] == -1) {
				q.push(nv);
				visited[nv] = visited[v] + 1;
			}
		}
	}
}

int main() {
	int n, k;

	cin >> n >> k;

	bfs(n, k);

	return 0;
}
