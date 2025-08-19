#include <iostream>
#include <vector>
#include <deque>

using namespace std;
const int MAX = 100001;

int bfs(int n, int k) {
    deque<int> dq;
    vector<int> visited(MAX, 0);

    dq.push_back(n);
    visited[n] = 1;

    while (!dq.empty()) {
        int x = dq.front();
        dq.pop_front();

        if (x == k)
            return visited[x] - 1;

        for (int nx : { x * 2, x - 1, x + 1 }) {
            if (nx < 0 || nx >= MAX) continue;
            if (visited[nx]) continue;

            if (nx == x * 2) {
                dq.push_back(nx);
                visited[nx] = visited[x];
            }
            else {
                dq.push_back(nx);
                visited[nx] = visited[x] + 1;
            }
        }
    }

    return -1;
}

int main() {
    int n, k;

    cin >> n >> k;

    cout << bfs(n, k);

    return 0;
}
