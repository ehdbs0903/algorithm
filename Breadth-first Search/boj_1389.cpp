#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int bfs(int v, int n, const vector<vector<int>>& graph) {
	vector<int> kevin_bacon(n + 1, -1);
	queue<int> q;
	int sum = 0;

	q.push(v);
	kevin_bacon[v] = 0;

	while (!q.empty()) {
		v = q.front();
		q.pop();

		for (int nv : graph[v]) {
			if (kevin_bacon[nv] == -1) {
				q.push(nv);
				kevin_bacon[nv] = kevin_bacon[v] + 1;
			}
		}
	}
	
	for (int i = 1; i < n + 1; i++)
		sum += kevin_bacon[i];
	
	return sum;
}


int main() {
	int n, m;

	cin >> n >> m;

	vector<vector<int>> graph(n + 1);
	vector<pair<int, int>> kevin_bacons;

	while (m--) {
		int v1, v2;

		cin >> v1 >> v2;

		graph[v1].emplace_back(v2);
		graph[v2].emplace_back(v1);
	}

	for (int i = 1; i < n + 1; i++) {
		kevin_bacons.emplace_back(bfs(i, n, graph), i);
	}

	sort(kevin_bacons.begin(), kevin_bacons.end());

	cout << kevin_bacons[0].second;

	return 0;
}
