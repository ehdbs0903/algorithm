#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void bfs(int v, vector<vector<int>>& graph, vector<int>& visited) {
	queue<int> q;

	q.push(v);
	visited[v] = 1;
	
	while (!q.empty()) {
		v = q.front();
		q.pop();

		for (int nv : graph[v]) {
			if (!visited[nv]) {
				q.push(nv);
				visited[nv] = 1;
			}
		}
	}
}

int main() {
	int n, m;
	cin >> n >> m;

	vector<vector<int>> graph(n + 1);
	while (m--) {
		int u, v;
		cin >> u >> v;

		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	vector<int> visited(n + 1);
	int cnt = 0;

	for (int i = 1; i <= n; i++) {
		if (!visited[i]) {
			bfs(i, graph, visited);
			cnt++;
		}
	}

	cout << cnt;

	return 0;
}
