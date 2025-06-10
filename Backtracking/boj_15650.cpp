#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int n, m;

void recursion(int idx, vector<int>& nums) {
	nums.push_back(idx + 1);
	
	if (nums.size() == m) {
		for (int num : nums)
			cout << num << " ";
		cout << "\n";
	}
	else {
		for (int i = idx + 1; i + m - nums.size() <= n; i++) {
			recursion(i, nums);
		}
	}

	nums.pop_back();
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> n >> m;

	vector<int> nums;

	for (int i = 0; i < n - m + 1; i++) {
		recursion(i, nums);
	}

	return 0;
}
