#include <iostream>
#include <vector>
using namespace std;

int main() {
    string s1, s2;
	cin >> s1 >> s2;

	int n = s1.size(), m = s2.size();
	vector<int> temp(m + 1);
	vector<int> next(m + 1);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (s1[i - 1] == s2[j - 1])
				next[j] = temp[j - 1] + 1;
			else
				next[j] = max(temp[j], next[j - 1]);
		}

		swap(temp, next);
	}

	cout << temp[m] << endl;

    return 0;
}
