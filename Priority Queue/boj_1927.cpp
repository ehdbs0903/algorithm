#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n;

	cin >> n;

	priority_queue<int, vector<int>, greater<int>> minHeap;

	while (n--) {
		int x;

		cin >> x;

		if (x == 0) {
			if (minHeap.empty())
				cout << 0;
			else {
				cout << minHeap.top();
				minHeap.pop();
			}
			cout << "\n";
			continue;
		}
		minHeap.push(x);
	}

	return 0;
}
