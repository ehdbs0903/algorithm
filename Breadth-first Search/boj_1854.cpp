#include <iostream>
#include <vector>
#include <queue>

using namespace std;
constexpr int INF = 1e9;

struct Compare {
    bool operator()(const pair<int, int>& a, const pair<int, int>& b) const {
        return a.second > b.second;
    }
};

vector<int> dijkstra(int k, const vector<vector<pair<int, int>>>& graph) {
    int n = graph.size() - 1;

    priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> pq;
    vector<priority_queue<int>> dist(n + 1);

    pq.emplace(1, 0);
    dist[1].push(0);

    while (!pq.empty()) {
        auto [v, w] = pq.top();
        pq.pop();

        if (dist[v].size() == k && dist[v].top() < w)
            continue;

        for (auto& [nv, nw] : graph[v]) {
            int nd = w + nw;

            if (dist[nv].size() < k) {
                dist[nv].push(nd);
                pq.emplace(nv, nd);
            }
            else if (dist[nv].top() > nd) {
                dist[nv].pop();
                dist[nv].push(nd);
                pq.emplace(nv, nd);
            }
        }
    }

    vector<int> result(n + 1, -1);

    for (int i = 1; i <= n; ++i) {
        if (dist[i].size() == k)
            result[i] = dist[i].top();
    }

    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;

    cin >> n >> m >> k;

    vector<vector<pair<int, int>>> graph(n + 1);

    for (int i = 0; i < m; ++i) {
        int a, b, c;

        cin >> a >> b >> c;

        graph[a].emplace_back(b, c);
    }

    auto dist = dijkstra(k, graph);

    for (int i = 1; i <= n; ++i) {
        cout << ((dist[i] == -1) ? -1 : dist[i]) << "\n";
    }

    return 0;
}
