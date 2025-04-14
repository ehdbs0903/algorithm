#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;
long long n;

using matrix = vector<vector<long long>>;

matrix multiply(const matrix& A, const matrix& B) {
	matrix C(2, vector<long long>(2, 0));

	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			for (int k = 0; k < 2; k++) {
				C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
			}
		}
	}

	return C;
}

matrix power(matrix A, long long exp) {
	matrix result(2, vector<long long>(2, 0));

	for (int i = 0; i < 2; i++) {
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

	cin >> n;

	matrix A = { {1, 1}, {1, 0} };

	cout << power(A, n)[0][1];

	return 0;
}
