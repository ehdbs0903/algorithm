#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> dijkstra(const int& s, const vector<vector<pair<int, int>>>& graph) {
	auto compare = [](const pair<int, int>& a, const pair<int, int>& b) {
		return a.second > b.second;
		};
	priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(compare)> pq(compare);
	vector<int> visited(graph.size(), -1);

	pq.push(make_pair(s, 0));

	while (!pq.empty()) {
		int v = pq.top().first;
		int w = pq.top().second;
		pq.pop();

		if (visited[v] != -1)
			continue;

		visited[v] = w;

		for (const auto& g : graph[v]) {
			int nv = g.first;
			int nw = g.second;

			if (visited[nv] != -1)
				continue;

			pq.push(make_pair(nv, w + nw));
		}
	}

	return visited;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int v, e, k;

	cin >> v >> e;
	cin >> k;

	vector<vector<pair<int, int>>> graph(v + 1);

	while (e--) {
		int s, e, w;

		cin >> s >> e >> w;

		graph[s].push_back(make_pair(e, w));
	}

	vector<int> result = dijkstra(k, graph);

	for (int i = 1; i <= v; i++) {
		if (result[i] == -1)
			cout << "INF";
		else
			cout << result[i];
		cout << "\n";
	}

	return 0;
}
