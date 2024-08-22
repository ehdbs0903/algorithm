#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    int t;

    cin >> t;

    while (t--) {
        int n;

        cin >> n;

        unordered_map<string, int> mp;

        while (n--) {
            string name, type;

            cin >> name >> type;

            mp[type]++;
        }

        int result = 1;

        for (auto k : mp) {
            result *= k.second + 1;
        }

        cout << result - 1 << "\n";
    }

    return 0;
}
