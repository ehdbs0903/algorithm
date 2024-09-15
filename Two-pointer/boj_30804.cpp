#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    int n;

    cin >> n;

    vector<int> fruits(n);

    for (int i = 0; i < n; i++) {
        cin >> fruits[i];
    }

    unordered_map<int, int> cnt;
    int left = 0, max_len = 0;

    for (int right = 0; right < n; right++) {
        cnt[fruits[right]]++;

        while (cnt.size() > 2) {
            cnt[fruits[left]]--;

            if (cnt[fruits[left]] == 0) {
                cnt.erase(fruits[left]);
            }

            left++;
        }

        max_len = max(max_len, right - left + 1);
    }

    cout << max_len;

    return 0;
}
