#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int bfs(int n, const vector<vector<int>>& graph) {
    int v, cnt = 0;
    queue<int> q;
    vector<int> visited(n + 1);
    
    q.push(1);
    visited[1] = 1;

    while (!q.empty()) {
        v = q.front();
        q.pop();
        cnt++;

        for (int nv : graph[v]) {
            if (!visited[nv]) {
                q.push(nv);
                visited[nv] = 1;
            }
        }
    }

    return cnt - 1;
}


int main() {
    int n, m;

    cin >> n;
    cin >> m;

    vector<vector<int>> graph(n + 1);

    while (m--) {
        int s, e;

        cin >> s >> e;

        graph[s].emplace_back(e);
        graph[e].emplace_back(s);
    }

    cout << bfs(n, graph);

    return 0;
}
