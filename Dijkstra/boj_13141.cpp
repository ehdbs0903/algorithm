#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <iomanip>

using namespace std;

struct Compare {
    bool operator()(const pair<int, double>& a, const pair<int, double>& b) {
        return a.second > b.second;
    }
};

double dijkstra(int v, const int& n, const vector<vector<pair<int, int>>>& graph) {
    priority_queue<pair<int, double>, vector<pair<int, double>>, Compare> pq;
    vector<double> dist(n + 1, 1e9);

    pq.push({ v, 0 });
    dist[v] = 0;

    while (!pq.empty()) {
        v = pq.top().first;
        double w = pq.top().second;
        pq.pop();

        if (w > dist[v])
            continue;

        for (auto p : graph[v]) {
            int nv = p.first;
            double nw = p.second;

            if (w + nw >= dist[nv])
                continue;

            pq.push({ nv, w + nw });
            dist[nv] = w + nw;
        }
    }

    double maxTime = 0.0f;

    for (int u = 1; u <= n; ++u) {
        maxTime = max(maxTime, dist[u]);
    }

    for (int u = 1; u <= n; ++u) {
        for (auto& e : graph[u]) {
            int v = e.first;
            double l = e.second;

            if (u <= v) {
                double tu = dist[u];
                double tv = dist[v];
                double diff = fabs(tu - tv);
                double finish;

                if (diff >= l)
                    finish = min(tu, tv) + l;
                else
                    finish = (tu + tv + l) / 2.0f;

                maxTime = max(maxTime, finish);
            }
        }
    }

    return maxTime;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;

    cin >> n >> m;

    vector<vector<pair<int, int>>> graph(n + 1);

    while (m--) {
        int s, e, l;

        cin >> s >> e >> l;

        graph[s].push_back({ e, l });
        graph[e].push_back({ s, l });
    }

    double ans = 1e9;

    for (int i = 1; i <= n; i++) {
        ans = min(ans, dijkstra(i, n, graph));
    }

    cout << fixed << setprecision(1) << ans;

    return 0;
}
