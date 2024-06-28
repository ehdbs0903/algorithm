#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	int n, m;
	
	cin >> n;

	unordered_map<int, int> card_count;
	int card;

	while (n--) {
		cin >> card;
		card_count[card] += 1;
	}

	cin >> m;

	while (m--) {
		cin >> card;
		cout << card_count[card] << " ";
	}

	return 0;
}
