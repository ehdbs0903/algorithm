#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
using namespace std;

int dijkstra(int v, const int target, const int n, const vector<vector<pair<int, int>>>& graph) {
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	vector<int> visited(n+1);
	int w = 0;
	
	pq.push(make_pair(0, v));

	while (!pq.empty()) {
		tie(w, v) = pq.top();
		pq.pop();

		if (v == target)
			return w;

		visited[v] = 1;

		for (auto g: graph[v]) {
			int nv = g.first;
			int nw = g.second;

			if (!visited[nv]) {
				pq.push(make_pair(nw + w, nv));
			}
		}
	}
}

bool compare(int a, int b) {
	return a < b;
}

int main() {
	int n, m, x;

	cin >> n >> m >> x;

	vector<vector<pair<int, int>>> graph(n+1);

	while (m--) {
		int u, v, w;

		cin >> u >> v >> w;

		graph[u].push_back(make_pair(v, w));
	}

	vector<int> times(n+1);
	
	for (int i = 1; i <= n; i++) {
		int time = 0;

		time += dijkstra(i, x, n, graph);
		time += dijkstra(x, i, n, graph);

		times[i] = time;
	}

	cout << *max_element(times.begin(), times.end());

	return 0;
}
