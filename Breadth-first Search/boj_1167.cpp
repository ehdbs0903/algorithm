#include <iostream>
#include <vector>
#include <queue>

using namespace std;

pair<int, int> bfs(int v, int n, const vector<vector<pair<int, int>>>& graph) {
    queue<pair<int, int>> q;
    vector<int> visited(n+1);

    q.push(make_pair(v, 0));
    visited[v] = 1;
    int fartestV = v;
    int fartestW = 0;

    while (!q.empty()) {
        v = q.front().first;
        int w = q.front().second;
        q.pop();

        if (w > fartestW) {
            fartestV = v;
            fartestW = w;
        }

        for (auto p : graph[v]) {
            int nv = p.first;
            int nw = p.second;

            if (!visited[nv]) {
                q.push(make_pair(nv, w + nw));
                visited[nv] = 1;
            }
        }
    }

    return make_pair(fartestV, fartestW);
}

int main() {
    int n;
    cin >> n;

    vector<vector<pair<int, int>>> graph(n+1);

    for (int i = 0; i < n; i++) {
        int v1;
        cin >> v1;

        while (true) {
            int v2;
            cin >> v2;

            if (v2 == -1)
                break;

            int w;
            cin >> w;

            graph[v1].emplace_back(v2, w);
        }
    }

    int v = bfs(1, n, graph).first;
 
    cout << bfs(v, n, graph).second;

    return 0;
}
