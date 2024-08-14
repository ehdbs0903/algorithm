#include <iostream>
using namespace std;

int main() {
    int t;

    cin >> t;

    while(t--) {
        int m, n, x, y;
        
        cin >> m >> n >> x >> y;

        int found = -1;

        while (x <= m * n) {
            if (x % n == y % n) {
                found = x;
                break;
            }

            x += m;
        }

        cout << found << "\n";
    }

    return 0;
}
