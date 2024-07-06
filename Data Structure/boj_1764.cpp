#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int n, m;

	cin >> n >> m;

	map<string, int> mp;
	vector<string> arr;

	for (int i = 0; i < n + m; i++) {
		string name;

		cin >> name;

		mp[name] += 1;
	}

	for (auto pair : mp) {
		if (pair.second == 2)
			arr.emplace_back(pair.first);
	}

	cout << arr.size() << "\n";
	for (auto a : arr)
		cout << a << "\n";

	return 0;
}
