#include <iostream>
#include <vector>
using namespace std;

int cnt = 0;

void nQueens(int n, int row, vector<bool>& col, vector<bool>& diag, vector<bool>& antiDiag) {
    if (row == n) {
        cnt++;
        return;
    }
    for (int c = 0; c < n; c++) {
        int d = row - c + n - 1;
        int a = row + c;
        if (!col[c] && !diag[d] && !antiDiag[a]) {
            col[c] = diag[d] = antiDiag[a] = true;
            nQueens(n, row + 1, col, diag, antiDiag);
            col[c] = diag[d] = antiDiag[a] = false;
        }
    }
}

int main() {
    int n;
    cin >> n;
    vector<bool> col(n, false);
    vector<bool> diag(2 * n - 1, false);
    vector<bool> antiDiag(2 * n - 1, false);
    nQueens(n, 0, col, diag, antiDiag);
    cout << cnt;
    return 0;
}
