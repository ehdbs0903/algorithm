#include <iostream>
#include <vector>
using namespace std;

struct Edge {
    int s, e, w;
};

bool bellmanFord(const vector<Edge>& edges, const int& N) {
    vector<int> dist(N + 1, 0);

    for (int i = 1; i <= N; ++i) {
        for (const auto& edge : edges) {
            if (dist[edge.e] > dist[edge.s] + edge.w) {
                dist[edge.e] = dist[edge.s] + edge.w;

                if (i == N) {
                    return true;
                }
            }
        }
    }

    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int TC;
    cin >> TC;

    while (TC--) {
        int N, M, W;
        cin >> N >> M >> W;

        vector<Edge> edges;

        for (int i = 0; i < M; ++i) {
            int S, E, T;
            cin >> S >> E >> T;
            edges.push_back({ S, E, T });
            edges.push_back({ E, S, T });
        }

        for (int i = 0; i < W; ++i) {
            int S, E, T;
            cin >> S >> E >> T;
            edges.push_back({ S, E, -T });
        }

        

        cout << (bellmanFord(edges, N) ? "YES\n" : "NO\n");
    }

    return 0;
}
