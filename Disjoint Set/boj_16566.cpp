#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <sstream>

using namespace std;

vector<int> parent;
vector<int> cards;

int find_parent(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find_parent(parent[x]);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, K;
    cin >> N >> M >> K;

    ostringstream os;

    cards.resize(M);
    for (int i = 0; i < M; i++) {
        cin >> cards[i];
    }
    sort(cards.begin(), cards.end());

    parent.resize(M + 1);
    iota(parent.begin(), parent.end(), 0);

    while (K--) {
        int x;
        cin >> x;

        int idx = upper_bound(cards.begin(), cards.end(), x) - cards.begin();
        int avail = find_parent(idx);

    	os << cards[avail] << "\n";

        parent[avail] = avail + 1;
    }

    cout << os.str();

    return 0;
}
