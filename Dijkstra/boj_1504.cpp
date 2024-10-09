#include <iostream>
#include <vector>
#include <queue>
using namespace std;

auto compare = [](pair<int, int> a, pair<int, int> b) {
	return a.first > b.first;
};

int dijkstra(int v, int target, const vector<vector<pair<int, int>>>& graph) {
	priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(compare)> pq(compare);
	vector<int> visited(graph.size());

	pq.push(make_pair(0, v));

	while (!pq.empty()) {
		int w = pq.top().first;
		v = pq.top().second;
		pq.pop();

		if (v == target)
			return w;

		visited[v] = 1;

		for (auto g : graph[v]) {
			int nv = g.first;
			int nw = g.second;

			if (visited[nv])
				continue;
			
			pq.push(make_pair(w + nw, nv));
		}
	}
}

int main() {
	int n, e;

	cin >> n >> e;

	vector<vector<pair<int, int>>> graph(n+1);

	while (e--) {
		int a, b, c;

		cin >> a >> b >> c;

		graph[a].emplace_back(b, c);
		graph[b].emplace_back(a, c);
	}

	int v1, v2;

	cin >> v1 >> v2;
	
	int dist1 = dijkstra(1, v1, graph) + dijkstra(v1, v2, graph) + dijkstra(v2, n, graph);
	int dist2 = dijkstra(1, v2, graph) + dijkstra(v2, v1, graph) + dijkstra(v1, n, graph);

	cout << min(dist1, dist2);


	return 0;
}
