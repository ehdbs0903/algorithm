#include <iostream>
#include <queue>
#include <cmath>
using namespace std;

struct Compare {
	bool operator()(int a, int b) {
		if (abs(a) != abs(b)) {
			return abs(a) > abs(b);
		}
		return a > b;
	}
};

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;

	cin >> n;

	priority_queue<int, vector<int>, Compare> pq;

	while (n--) {
		int x;

		cin >> x;

		if (x) {
			pq.push(x);
		}
		else {
			if (!pq.empty()) {
				cout << pq.top() << "\n";
				pq.pop();
			}
			else {
				cout << 0 << "\n";
			}
		}
	}

	return 0;
}
