#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

pair<int ,int> bfs(int v, const int n, const vector<vector<pair<int, int>>>& graph) {
	queue<int> q;
	vector<int> visited(n + 1);

	q.push(v);
	visited[v] = 1;

	while (!q.empty()) {
		v = q.front();
		q.pop();

		for (const auto& p : graph[v]) {
			int nv = p.first;
			int w = p.second;

			if (!visited[nv]) {
				q.push(nv);
				visited[nv] = visited[v] + w;
			}
		}
	}

	auto it = max_element(visited.begin(), visited.end());

	return { it - visited.begin(), *it};
}

int main() {
	int n;

	cin >> n;

	vector<vector<pair<int, int>>> graph(n + 1);

	for (int i = 0; i < n - 1; i++) {
		int s, e, w;

		cin >> s >> e >> w;

		graph[s].push_back({ e, w });
		graph[e].push_back({ s, w });
	}

	auto p = bfs(1, n, graph);
	auto np = bfs(p.first, n, graph);

	cout << np.second - 1;

	return 0;
}
