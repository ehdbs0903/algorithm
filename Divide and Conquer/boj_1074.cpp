#include <iostream>
using namespace std;

int ans = 0;

void recursion(int n, int x, int y) {
	if (n == 0) {
		ans += x * 2 + y;
		cout << ans;
		return;
	}

    if (x < (1 << n) && y < (1 << n)) {
        recursion(n - 1, x, y);
    }
    else if (x < (1 << n) && y >= (1 << n)) {
        ans += (1 << (2 * n));
        recursion(n - 1, x, y - (1 << n));
    }
    else if (x >= (1 << n) && y < (1 << n)) {
        ans += 2 * (1 << (2 * n));
        recursion(n - 1, x - (1 << n), y);
    }
    else {
        ans += 3 * (1 << (2 * n));
        recursion(n - 1, x - (1 << n), y - (1 << n));
    }
}

int main() {
	int n, r, c;

	cin >> n >> r >> c;

	recursion(n, r, c);

	return 0;
}
