#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {
	int n, k;

	cin >> n >> k;

	queue<int> q;
	string ans = "<";
	
    for (int i = 0; i < n; i++)
        q.push(i + 1);

    while (!q.empty()) {
        for (int i = 0; i < k-1; i++) {
            q.push(q.front());
            q.pop();
        }

        ans += to_string(q.front()) + ", ";
        q.pop();
    }

	ans = ans.substr(0, ans.size() - 2);
	ans += ">";
    
	cout << ans;
	
	return 0;
}
