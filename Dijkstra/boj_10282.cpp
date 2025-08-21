#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Compare {
    bool operator()(const pair<int, int>& a, const pair<int, int>& b) {
        return a.second > b.second;
    }
};

pair<int, int> dijkstra(int start, const int n, const vector<vector<pair<int, int>>>& graph) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> pq;
    vector<int> dist(n + 1, 1e9);

    pq.emplace(start, 0);
    dist[start] = 0;

    while (!pq.empty())
    {
        int v = pq.top().first;
        int w = pq.top().second;
        pq.pop();

        if (dist[v] < w)
            continue;

        for (auto p : graph[v]) {
            int nv = p.first;
            int nw = p.second;

            if (w + nw >= dist[nv])
                continue;

            pq.emplace(nv, w + nw);
            dist[nv] = w + nw;
        }
    }

    int cnt = 0;
    int max_time = 0;

    for (int i = 1; i < n + 1; i++) {
        if (dist[i] != 1e9) {
            cnt++;
            max_time = max(max_time, dist[i]);
        }
    }

    return { cnt, max_time };
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n, d, c;
        cin >> n >> d >> c;

        vector<vector<pair<int, int>>> graph(n + 1);

        for (int i = 0; i < d; i++) {
            int a, b, s;
            cin >> a >> b >> s;

            graph[b].emplace_back(a, s);
        }

        pair<int, int> result = dijkstra(c, n, graph);
        cout << result.first << " " << result.second << "\n";
    } 

    return 0;
}
