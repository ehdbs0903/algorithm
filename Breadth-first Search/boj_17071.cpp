#include <iostream>
#include <queue>

using namespace std;

const int MAX = 500000;

int N, K;
bool visited[2][MAX + 1];

int bfs() {
    if (N == K) return 0;

    queue<pair<int, int>> q;
    q.push({ N, 0 });
    visited[0][N] = true;

    int time = 0;
    while (true) {
        int brother = K + time * (time + 1) / 2;
        if (brother > MAX) return -1;
        if (visited[time % 2][brother]) return time;

        int qSize = q.size();
        for (int i = 0; i < qSize; ++i) {
            auto [cur, t] = q.front();
            q.pop();

            for (int next : {cur - 1, cur + 1, cur * 2}) {
                if (next < 0 || next > MAX) continue;
                if (visited[(t + 1) % 2][next]) continue;

                visited[(t + 1) % 2][next] = true;
                q.push({ next, t + 1 });
            }
        }
        time++;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K;
    cout << bfs() << '\n';
    return 0;
}
