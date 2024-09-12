#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main() {
    int n;

    cin >> n;

    vector<int> x;

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        
        x.push_back(num);
    }

    vector<int> copy = x;

    sort(copy.begin(), copy.end());

    unordered_map<int, int> mp;
    int mapping = 0;

    for (auto num: copy) {
        if (mp.find(num) == mp.end())
            mp[num] = mapping++;
    }

    for (auto num: x) {
        cout << mp[num] << " ";
    }

    return 0;
}
