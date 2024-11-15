#include <iostream>
#include <vector>
#include <stack>
#include <tuple>

using namespace std;

int dfs(const int& r, const int& c, const vector<string>& board) {
    int dx[] = { -1, 1, 0, 0 };
    int dy[] = { 0, 0, -1, 1 };

    stack<tuple<int, int, int, int>> s;
    int ret = 0;

    int initialMask = 1 << (board[0][0] - 'A');
    s.push({ 0, 0, initialMask, 1 });

    while (!s.empty()) {
        int x = get<0>(s.top());
        int y = get<1>(s.top());
        int mask = get<2>(s.top());
        int length = get<3>(s.top());
        s.pop();

        ret = max(ret, length);

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= r || ny < 0 || ny >= c)
                continue;

            int nextCharBit = 1 << (board[nx][ny] - 'A');

            if (mask & nextCharBit)
                continue;

            s.push({ nx, ny, mask | nextCharBit, length + 1 });
        }
    }

    return ret;
}

int main() {
    int r, c;
    cin >> r >> c;

    vector<string> board(r);
    for (int i = 0; i < r; i++) {
        cin >> board[i];
    }

    cout << dfs(r, c, board) << '\n';
    return 0;
}
