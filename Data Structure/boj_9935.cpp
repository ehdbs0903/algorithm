#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, bomb;
    cin >> s >> bomb;

    int n = bomb.size();
    char lastChar = bomb[n - 1];

    string stack;

    for (char c : s) {
        stack.push_back(c);

        if (c == lastChar && stack.size() >= n) {
            bool match = true;
            for (int i = 0; i < n; i++) {
                if (stack[stack.size() - n + i] != bomb[i]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                stack.erase(stack.size() - n, n);
            }
        }
    }

    cout << (stack.empty() ? "FRULA" : stack);
    return 0;
}
