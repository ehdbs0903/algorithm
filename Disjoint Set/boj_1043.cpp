#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

unordered_map<int, int> parent;

int find(int v) {
    if (parent[v] != v) {
        parent[v] = find(parent[v]);
    }

    return parent[v];
}

void union_set(int a, int b) {
    a = find(a);
    b = find(b);

    if (a > b) {
        parent[a] = b;
    }
    else {
        parent[b] = a;
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    int factNum;
    cin >> factNum;

    while (factNum--) {
        int factKnown;
        cin >> factKnown;

        parent[factKnown] = 0;
    }

    vector<vector<int>> parties(m);

    for (int i = 0; i < m; i++) {
        int partyNum;
        cin >> partyNum;

        parties[i].resize(partyNum);

        for (int j = 0; j < partyNum; j++) {
            cin >> parties[i][j];

            if (parent.find(parties[i][j]) == parent.end())
                parent[parties[i][j]] = parties[i][j];
        }

        for (int j = 1; j < partyNum; j++) {
            union_set(parties[i][0], parties[i][j]);
        }
    }

    int cnt = 0;

    for (int i = 0; i < m; i++) {
        bool canLie = true;

        for (int j = 0; j < parties[i].size(); j++) {
            if (find(parties[i][j]) == 0) {
                canLie = false;
                break;
            }
        }

        if (canLie) {
            cnt++;
        }
    }

    cout << cnt;

    return 0;
}
