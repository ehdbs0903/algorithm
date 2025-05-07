#include <iostream>
#include <vector>

using namespace std;

vector<int> pre;

void postorder(int start, int end) {
    if (start >= end) return;

    int root = pre[start];
    int idx = start + 1;
    
    while (idx < end && pre[idx] < root)
        idx++;

    postorder(start + 1, idx);
    postorder(idx, end);

    cout << root << "\n";
}

int main() {
    int n;

    while (cin >> n) {
        pre.push_back(n);
    }

    postorder(0, pre.size());

    return 0;
}
