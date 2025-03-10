#include <iostream>
#include <algorithm>
#include <tuple>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int a, b, c;
    cin >> a >> b >> c;
    int max0 = a, max1 = b, max2 = c;
    int min0 = a, min1 = b, min2 = c;

    for (int i = 1; i < n; i++) {
        cin >> a >> b >> c;

        auto newMax0 = a + max(max0, max1);
        auto newMax1 = b + max({ max0, max1, max2 });
        auto newMax2 = c + max(max1, max2);

        auto newMin0 = a + min(min0, min1);
        auto newMin1 = b + min({ min0, min1, min2 });
        auto newMin2 = c + min(min1, min2);

        tie(max0, max1, max2) = make_tuple(newMax0, newMax1, newMax2);
        tie(min0, min1, min2) = make_tuple(newMin0, newMin1, newMin2);
    }

    cout << max({ max0, max1, max2 }) << " " << min({ min0, min1, min2 }) << "\n";

    return 0;
}
