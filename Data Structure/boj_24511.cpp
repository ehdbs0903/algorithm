#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;

    cin >> n;

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    deque<int> dq;
    int num;

    for (int i = 0; i < n; i++) {

        cin >> num;

        if (!a[i])
            dq.push_back(num);
    }

    int m;
    
    cin >> m;

    for (int i = 0; i < m; i++) {
        cin >> num;

        dq.push_front(num);
        cout << dq[dq.size() - 1] << " ";
        dq.pop_back();
    }

    return 0;
}
