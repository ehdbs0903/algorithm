#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int D(int x) {
    return (x * 2) % 10000;
}

int S(int x) {
    return (x > 0) ? x - 1 : 9999;
}

int L(int x) {
    return (x % 1000) * 10 + x / 1000; 
}

int R(int x) {
    return x / 10 + (x % 10) * 1000;
}

string bfs(int x, int target) {
    int (*op[4])(int x) = {D, S, L, R};
    char label[4] = {'D', 'S', 'L', 'R'};
    vector<int> visited(10000, -1);  // int로 초기화
    queue<pair<int, string>> q;

    q.push(make_pair(x, ""));
    visited[x] = 1;

    while (!q.empty()) {
        int curr = q.front().first;
        string route = q.front().second;
        q.pop();

        if (curr == target)
            return route;

        for (int i = 0; i < 4; i++) {
            int nx = op[i](curr);

            if (visited[nx] == -1) {
                q.push(make_pair(nx, route + label[i]));
                visited[nx] = 1;
            }
        }
    }

    return "";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;

    while (t--) {
        int a, b;
        cin >> a >> b;
        cout << bfs(a, b) << "\n";
    }

    return 0;
}
