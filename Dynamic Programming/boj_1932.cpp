#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
    
    int n;
    cin >> n;

    vector<int> dp(n);
    cin >> dp[0];

    for (int i = 1; i < n; i++) {
        vector<int> temp(i + 1);
        for (int j = 0; j <= i; j++) {
            int num;
            cin >> num;

            if (j == 0)
                temp[j] = dp[j] + num;
            else if (j == i)
                temp[j] = dp[j - 1] + num;
            else
                temp[j] = max(dp[j - 1], dp[j]) + num;
        }
        dp = move(temp);
    }

    cout << *max_element(dp.begin(), dp.end());
    return 0;
}
