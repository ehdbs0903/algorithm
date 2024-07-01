#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;

    cin >> t;

    int n;
    int dp[41][2] = { {1, 0}, {0, 1} };

    for (int i = 2; i < 41; i++) {
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0];
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1];
    }

    while (t--) {
        cin >> n;

        cout << dp[n][0] << " " << dp[n][1] << "\n";
    }

	return 0;
}
