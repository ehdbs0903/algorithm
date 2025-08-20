#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

string find(string name, unordered_map<string, string>& parent) {
    if (name == parent[name])
        return name;
    return parent[name] = find(parent[name], parent);
}

int unite(string a, string b, unordered_map<string, string>& parent, unordered_map<string, int>& sz) {
    string ra = find(a, parent);
    string rb = find(b, parent);

    if (ra == rb)
        return sz[ra];

    if (ra < rb)
        swap(ra, rb);

    parent[rb] = ra;
    sz[ra] += sz[rb];

    return sz[ra];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int f;
        cin >> f;

        unordered_map<string, string> parent;
        unordered_map<string, int> sz;

        for (int i = 0; i < f; i++) {
            string a, b;
            cin >> a >> b;

            if (!sz[a]) {
                parent[a] = a;
                sz[a] = 1;
            }
            if (!sz[b]) {
                parent[b] = b;
                sz[b] = 1;
            }

            cout << unite(a, b, parent, sz) << "\n";
        }
    }
    return 0;
}
