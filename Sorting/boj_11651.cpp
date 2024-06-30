#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool compare(const pair<int, int>& a, const pair<int, int>& b) {
	if (a.second == b.second) {
		return a.first < b.first;
	}
	return a.second < b.second;
}



int main() {
	int n;

	cin >> n;

	vector<pair<int, int>> points;
	int x, y;

	while (n--) {
		cin >> x >> y;

		points.emplace_back(x, y);
	}

	sort(points.begin(), points.end(), compare);

	for (const auto& p: points)
		cout << p.first << " " << p.second << "\n";

	return 0;
}
