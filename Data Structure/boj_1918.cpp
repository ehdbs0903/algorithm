#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
    string expression;

    cin >> expression;

    unordered_map<char, int> precedence = {
        {'+', 1}, {'-', 1},
        {'*', 2}, {'/', 2},
        {'(', 0}, {')', 0}
    };
    stack<char> s;
    string result = "";

    for (char c : expression) {
        if (isalpha(c)) {
            result += c;
        }
        else if (c == '(') {
            s.push(c);
        }
        else if (c == ')') {
            while (!s.empty() && s.top() != '(') {
                result += s.top();
                s.pop();
            }
            s.pop();
        }
        else {
            while (!s.empty() && precedence[s.top()] >= precedence[c]) {
                result += s.top();
                s.pop();
            }
            s.push(c);
        }
    }

    while (!s.empty()) {
        result += s.top();
        s.pop();
    }

    cout << result << endl;
    return 0;
}
