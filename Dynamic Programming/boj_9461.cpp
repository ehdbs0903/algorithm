#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    long dp[101] = {};

    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 1;
    dp[4] = 2;
    dp[5] = 2;

    for (int i = 6; i < 101; i++)
        dp[i] = dp[i-1] + dp[i-5];

    int t;
    
    cin >> t;

    while (t--) {
        int n;
        
        cin >> n;

        cout << dp[n] << "\n";
    }

    return 0;
}
