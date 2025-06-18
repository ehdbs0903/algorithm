#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int MAX = 100000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<int> visited(MAX + 1, -1);
    vector<int> cnt(MAX + 1, 0);
    queue<int> q;

    visited[n] = 0;
    cnt[n] = 1;
    q.push(n);

    while (!q.empty()) {
        int x = q.front();
        q.pop();

        for (int nx : {x * 2, x - 1, x + 1}) {
            if (nx < 0 || nx > MAX)
                continue;

            if (visited[nx] == -1) {
                visited[nx] = visited[x] + 1;
                cnt[nx] = cnt[x];
                q.push(nx);
            }
            else if (visited[nx] == visited[x] + 1) {
                cnt[nx] += cnt[x];
            }
        }
    }

    cout << visited[k] << "\n"
        << cnt[k] << "\n";
    return 0;
}
