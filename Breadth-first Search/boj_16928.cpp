#include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>
using namespace std;

unordered_map<int, int> mp;

int bfs(int v) {
	queue<int> q;
	vector<int> visited(101);

	q.push(v);
	visited[v] = 1;

	while (!q.empty()) {
		v = q.front();
		q.pop();

		if (v == 100)
			return visited[v] - 1;

		for (int i = 1; i <= 6; i++) {
			int nv = v + i;

			if (nv > 100)
				continue;

			if (mp[nv]) {
				nv = mp[nv];
			}

			if (!visited[nv]) {
				q.push(nv);
				visited[nv] = visited[v] + 1;
			}
		}
	}
}

int main() {
	int n, m;
	cin >> n >> m;

	
	while (n--) {
		int x, y;
		cin >> x >> y;

		mp[x] = y;
	}

	while (m--) {
		int u, v;
		cin >> u >> v;

		mp[u] = v;
	}

	cout << bfs(1);

	return 0;
}
