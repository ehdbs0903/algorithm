#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, m, b;
    cin >> n >> m >> b;

    vector<vector<int>> board(n, vector<int>(m));
    int minHeight = 256, maxHeight = 0;
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> board[i][j];

            minHeight = min(minHeight, board[i][j]);
            maxHeight = max(maxHeight, board[i][j]);
        }
    }

    int time = 2147483647;
    int height = -1;

    for (int h = minHeight; h <= maxHeight; ++h) {
        int removedBlock = 0;
        int addedBlock = 0;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                int diff = board[i][j] - h;

                if (diff > 0) {
                    removedBlock += diff;
                } else {
                    addedBlock -= diff;
                }
            }
        }

        if (removedBlock + b >= addedBlock) {
            int t = removedBlock * 2 + addedBlock;
            
            if (t < time || (t == time && h > height)) {
                time = t;
                height = h;
            }
        }
    }

    cout << time << " " << height << endl;

    return 0;
}
