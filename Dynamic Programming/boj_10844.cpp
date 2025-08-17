#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1000000000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> current(10), next(10);

    for (int i = 1; i <= 9; i++)
        current[i] = 1;

    for (int i = 1; i < n; i++) {
        fill(next.begin(), next.end(), 0);

        for (int j = 0; j <= 9; j++) {
            if (j > 0)
                next[j - 1] = (next[j - 1] + current[j]) % MOD;
            if (j < 9)
                next[j + 1] = (next[j + 1] + current[j]) % MOD;
        }

        swap(current, next);
    }

    int sum = 0;
    for (int i = 0; i <= 9; i++) {
        sum = (sum + current[i]) % MOD;
    }

    cout << sum;
    return 0;
}
