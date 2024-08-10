#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n, m;
	int trees[1000000];

	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> trees[i];

	int start = 1, end = *max_element(trees, trees + n);
	int mid = 0;

	while (start <= end) {
		long long sum = 0;
		mid = (start + end) / 2;

		for (int i = 0; i < n; i++) {
			if (trees[i] > mid)
				sum += trees[i] - mid;
		}

		if (sum >= m)
			start = mid + 1;
		else
			end = mid - 1;
	}
	
	cout << end;

	return 0;
}
