#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while(t--) {
        int n;
        cin >> n;
        
        vector<vector<int>> score(2, vector<int>(n, 0));
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < n; j++) {
                cin >> score[i][j];
            }
        }
        
        if(n == 1) {
            cout << max(score[0][0], score[1][0]) << "\n";
            continue;
        }
        
        int prev0 = score[0][0], prev1 = score[1][0];
        int cur0 = prev1 + score[0][1];
        int cur1 = prev0 + score[1][1];
        
        for (int i = 2; i < n; i++) {
            int next0 = max(cur1, prev1) + score[0][i];
            int next1 = max(cur0, prev0) + score[1][i];
            
            prev0 = cur0;
            prev1 = cur1;
            cur0 = next0;
            cur1 = next1;
        }
        
        cout << max(cur0, cur1) << "\n";
    }
    
    return 0;
}
