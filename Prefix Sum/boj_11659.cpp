#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m;
	cin >> n >> m;

	vector<int> arr(n + 1);
	for (int i = 1; i < n + 1; i++)
		cin >> arr[i];

	for (int i = 1; i < n + 1; i++) {
		arr[i] += arr[i - 1];
	}

	while (m--) {
		int start, end;
		cin >> start >> end;

		cout << arr[end] - arr[start - 1] << "\n";
	}

	return 0;
}
