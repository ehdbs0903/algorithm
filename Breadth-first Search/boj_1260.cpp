#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

void dfs(int v, int n, const vector<vector<int>>& graph) {
	stack<int> s;
	vector<int> visited(n + 1);

	s.push(v);

	while (!s.empty()) {
		v = s.top();
		s.pop();

		if (!visited[v]) {
			visited[v] = 1;
			cout << v << " ";
		}

		for (int i = graph[v].size() - 1; i >= 0; --i) {
			int nv = graph[v][i];

			if (!visited[nv]) {
				s.push(nv);
			}
		}
	}
}

void bfs(int v, int n, const vector<vector<int>>& graph) {
	queue<int> q;
	vector<int> visited(n + 1);

	q.push(v);
	visited[v] = 1;

	while (!q.empty()) {
		v = q.front();
		cout << v << " ";
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
	int n, m, v;

	cin >> n >> m >> v;

	vector<vector<int>> graph(n+1);
	int v1, v2;

	while (m--) {
		cin >> v1 >> v2;
		
		graph[v1].emplace_back(v2);
		graph[v2].emplace_back(v1);
	}

	for (int i = 0; i <= n; i++)
		sort(graph[i].begin(), graph[i].end());

	dfs(v, n, graph);
	cout << "\n";
	bfs(v, n, graph);

	return 0;
}
