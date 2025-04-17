#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m;

	cin >> n >> m;

	vector<vector<int>> prefix_sum(n + 1, vector<int>(n + 1, 0));
	
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> prefix_sum[i][j];

			prefix_sum[i][j] += prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1];
		}
	}

	for (int i = 0; i < m; i++) {
		int x1, y1, x2, y2;

		cin >> x1 >> y1 >> x2 >> y2;

		cout << prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1] << "\n";
	}

	return 0;
}
