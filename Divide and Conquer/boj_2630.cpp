#include <iostream>
using namespace std;

int white = 0, blue = 0;
int board[128][128];

void recursion(int x, int y, int n) {
	for (int i = x; i < x + n; i++) {
		for (int j = y; j < y + n; j++) {
			if (board[i][j] != board[x][y]) {
				recursion(x, y, n/2);
				recursion(x + n/2, y, n/2);
				recursion(x, y + n/2, n/2);
				recursion(x + n/2, y + n/2, n/2);
				return;
			}
		}
	}
	
	if (board[x][y])
		blue++;
	else
		white++;
}

int main() {
	int n;

	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> board[i][j];
		}
	}

	recursion(0, 0, n);

	cout << white << "\n";
	cout << blue << "\n";

	return 0;
}
