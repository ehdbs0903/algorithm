#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int dijkstra(int v, const int target, const vector<vector<pair<int, int>>>& graph) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    vector<int> visited(graph.size());

    pq.push(make_pair(0, v));
    
    while (!pq.empty()) {
        int w = pq.top().first;
        v = pq.top().second;
        pq.pop();

        if (v == target)
            return w;

        if (visited[v]) continue;
        visited[v] = 1;

        for (auto p : graph[v]) {
            int nv = p.first;
            int nw = p.second;

            if (!visited[nv]) {
                pq.push(make_pair(w + nw, nv));
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;

    cin >> n >> m;

    vector<vector<pair<int, int>>> graph(n+1);

    while (m--) {
        int u, v, w;

        cin >> u >> v >> w;

        graph[u].push_back(make_pair(v, w));
    }

    int s, e;

    cin >> s >> e;

    cout << dijkstra(s, e, graph);

    return 0;
}
