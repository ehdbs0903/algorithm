#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;

    cin >> n >> m;

    unordered_map<string, string> mp;

    for (int i = 1; i < n + 1; i++) {
        string temp;

        cin >> temp;

        mp[to_string(i)] = temp;
        mp[temp] = to_string(i);
    }

    while (m--) {
        string temp;

        cin >> temp;

        cout << mp[temp] << "\n";
    }

    return 0;
}
