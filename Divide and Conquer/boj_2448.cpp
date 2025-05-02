#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> star;

void drawStars(int n) {
    if (n == 3) {
        star.push_back("  *  ");
        star.push_back(" * * ");
        star.push_back("*****");
        return;
    }

    drawStars(n / 2);

    vector<string> tmp;
    int half = n / 2;

    for (auto s : star) {
        tmp.push_back(string(half, ' ') + s + string(half, ' '));
    }

    for (auto s : star) {
        tmp.push_back(s + " " + s);
    }

    star = tmp;
}

int main() {
    int n;
    cin >> n;

    drawStars(n);
    for (auto s : star) {
        cout << s << "\n";
    }
    return 0;
}
