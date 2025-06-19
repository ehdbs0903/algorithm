#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    vector<pair<int, int>> items(N);
    for (int i = 0; i < N; ++i) {
        cin >> items[i].first >> items[i].second;
    }

    vector<int> dp(K + 1, 0);

    int w0 = items[0].first, v0 = items[0].second;
    for (int j = w0; j <= K; ++j) {
        dp[j] = v0;
    }

    for (int i = 1; i < N; ++i) {
        int w = items[i].first;
        int v = items[i].second;
        for (int j = K; j >= w; --j) {
            dp[j] = max(dp[j], dp[j - w] + v);
        }
    }

    cout << dp[K] << "\n";
    return 0;
}
