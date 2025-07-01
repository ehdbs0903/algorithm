#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000;
int n;

using matrix = vector<vector<int>>;

matrix multiply(const matrix& A, const matrix& B) {
    matrix C(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
            }
        }
    }
    return C;
}

matrix power(matrix A, long long exp) {
    matrix result(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++) {
        result[i][i] = 1;
    }

    while (exp > 0) {
        if (exp % 2 == 1)
            result = multiply(result, A);
        A = multiply(A, A);
        exp /= 2;
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    long long b;

    cin >> n >> b;

    matrix A(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> A[i][j];

            if (A[i][j] == 1000)
                A[i][j] = 0;
        }
    }

    matrix result = power(A, b);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << result[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
