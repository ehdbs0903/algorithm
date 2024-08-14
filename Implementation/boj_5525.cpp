#include <iostream>
#include <string>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    string s;
    cin >> s;

    int cnt = 0;
    int i = 0;

    while (i < m - 1) {
        if (s.substr(i, 3) == "IOI") {
            int k = 0;
            while (i + 2 < m && s.substr(i, 3) == "IOI") {
                k++;
                i += 2;
            }
            if (k >= n) {
                cnt += k - n + 1;
            }
        } else {
            i++;
        }
    }

    cout << cnt << endl;

    return 0;
}
