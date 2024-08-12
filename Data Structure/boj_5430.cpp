#include <iostream>
#include <deque>
#include <string>
#include <sstream>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        try {
            string s;
            cin >> s;

            int n;
            cin >> n;

            string arr;
            cin >> arr;

            deque<int> nums;
            string num;
            stringstream ss(arr.substr(1, arr.size() - 2));

            while (getline(ss, num, ',')) {
                if (!num.empty()) {
                    nums.push_back(stoi(num));
                }
            }

            int idx = 1;
            for (char ss : s) {
                if (ss == 'R') {
                    idx *= -1;
                } else if (ss == 'D') {
                    if (nums.empty()) {
                        throw "error";
                    }
                    if (idx < 0) {
                        nums.pop_back();
                    } else {
                        nums.pop_front();
                    }
                }
            }

            cout << "[";
            if (idx > 0) {
                for (size_t i = 0; i < nums.size(); i++) {
                    cout << nums[i];
                    if (i < nums.size() - 1) {
                        cout << ",";
                    }
                }
            } else {
                for (size_t i = nums.size(); i-- > 0;) {
                    cout << nums[i];
                    if (i > 0) {
                        cout << ",";
                    }
                }
            }
            cout << "]" << endl;

        } catch (...) {
            cout << "error" << endl;
        }
    }

    return 0;
}
