#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int n;

	cin >> n;

	vector<pair<int, int>> arr;
	int x, y;

	while (n--) {
		cin >> x >> y;

		arr.emplace_back(x, y);
	}

	sort(arr.begin(), arr.end());

	for (const auto& a: arr)
		cout << a.first << " " << a.second << "\n";

	return 0;
}
