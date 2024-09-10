#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    int n, m;

    cin >> n >> m;

    unordered_map<string, string> mp;

    while (n--) {
        string key, value;

        cin >> key >> value;

        mp[key] = value;
    }

    while (m--) {
        string key;

        cin >> key;

        cout << mp[key] << "\n";
    }

    return 0;
}
