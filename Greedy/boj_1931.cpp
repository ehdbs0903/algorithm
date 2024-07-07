#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;

    cin >> n;

    vector<pair<int, int>> time;

    while (n--) {
        int start, end;

        cin >> start >> end;

        time.emplace_back(end, start);
    }

    sort(time.begin(), time.end());

    int end = time[0].first, cnt = 1;

    for (int i = 1; i < time.size(); i++) {
        if (time[i].second >= end) {
            end = time[i].first;
            cnt++;
        }
    }

    cout << cnt;

    return 0;
}
