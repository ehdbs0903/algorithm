#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(const pair<int, string>& a, const pair<int, string>& b) {
	return a.first < b.first;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;

	cin >> n;

	vector<pair<int, string>> arr;

	int age;
	string name;

	while (n--) {
		cin >> age >> name;
		arr.emplace_back(age, name);
	}

	stable_sort(arr.begin(), arr.end(), compare);

	for (auto it : arr)
		cout << it.first << " " << it.second << "\n";

	return 0;
}
