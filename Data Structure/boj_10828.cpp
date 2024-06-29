#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

	int n;

	cin >> n;

	stack<int> s;
	string command;
  int num;

  while (n--) {
      cin >> command;

      if (command == "push") {
          cin >> num;
          s.push(num);
      }
      else if (command == "pop") {
          if (s.empty())
              cout << "-1\n";
          else {
              cout << s.top() << "\n";
              s.pop();
          }
      }
      else if (command == "size")
          cout << s.size() << "\n";
      else if (command == "empty")
          cout << (s.empty() ? 1 : 0) << "\n";
      else if (command == "top")
              cout << (s.empty() ? -1 : s.top()) << "\n";
  }

	return 0;
}
