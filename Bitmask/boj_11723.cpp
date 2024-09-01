#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int m, x, set = 0;
	cin >> m;

	while (m--) {
		string cmd;

		cin >> cmd;

		if (cmd == "add") {
			cin >> x;

			set |= (1 << x);
		}
		else if (cmd == "remove") {
			cin >> x;

			set &= ~(1 << x);
		}
		else if (cmd == "check") {
			cin >> x;

			if (set & (1 << x))
				cout << 1 << "\n";
			else
				cout << 0 << "\n";
		}
		else if (cmd == "toggle") {
			cin >> x;

			if (set & (1 << x))
				set &= ~(1 << x);
			else
				set |= (1 << x);
		}
		else if (cmd == "all") {
			set = (1 << 22) - 1;
		}
		else if (cmd == "empty") {
			set = 0;
		}
	}

	return 0;
}
