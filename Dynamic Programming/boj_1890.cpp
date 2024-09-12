#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;

    cin >> n;

    vector<vector<int>> board(n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> board[i][j];
        }
    }
    
    vector<vector<long long>> dp(n, vector<long long>(n));
    
    dp[0][0] = 1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int move = board[i][j];

            if (move <= 0) continue;

            if (i + move < n)
                dp[i+move][j] += dp[i][j];

            if (j + move < n)
                dp[i][j+move] += dp[i][j];
        }
    }

    cout << dp[n-1][n-1];

    return 0;
}
