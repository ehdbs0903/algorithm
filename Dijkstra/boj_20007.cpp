#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
using pii = pair<int, int>;

constexpr int INF = 1'000'000'000;

struct Compare {
    bool operator()(const pii& a, const pii& b) {
        return a.second > b.second;
    }
};

vector<int> dijkstra(int start, int n, const vector<vector<pii>>& graph) {
    priority_queue<pii, vector<pii>, Compare> pq;
    vector<int> dist(n, INF);

    pq.push({ start, 0 });
    dist[start] = 0;

    while (!pq.empty()) {
        int v = pq.top().first;
        int w = pq.top().second;
        pq.pop();

        if (dist[v] < w)
            continue;

        for (const auto& p : graph[v]) {
            int nv = p.first;
            int nw = p.second;

            if (dist[nv] < w + nw)
                continue;

            dist[nv] = w + nw;
            pq.push({ nv, w + nw });
        }
    }

    return dist;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, x, y;

    cin >> n >> m >> x >> y;

    vector<vector<pii>> graph(n);

    for (int i = 0; i < m; i++) {
        int a, b, c;

        cin >> a >> b >> c;

        graph[a].push_back({ b, c });
        graph[b].push_back({ a, c });
    }

    vector<int> dist = dijkstra(y, n, graph);

    sort(dist.begin(), dist.end());

    int day = 1;
    int tempDist = 0;
    int half = x / 2;

    for (int d : dist) {
        if (d > half) {
            day = -1;
            break;
        }
        
        if (tempDist + d > half) {
            tempDist = d;
            day++;
        }
        else {
            tempDist += d;
        }
    }

    cout << day;

    return 0;
}
