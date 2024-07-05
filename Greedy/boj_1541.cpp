#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

vector<string> split(const string& str, char delimiter) {
	vector<string> tokens;
	string token;
	stringstream ss(str);

	while (getline(ss, token, delimiter))
		tokens.push_back(token);
	
	return tokens;
}

int main() {
	string str;
	
	cin >> str;

	vector<string> parts;
	vector<int> nums;

	parts = split(str, '-');

	int sum = 0;

	for (int i = 0; i < parts.size(); i++) {
		vector<string> sub_parts = split(parts[i], '+');

		for (string num : sub_parts) {
			if (i == 0)
				sum += stoi(num);
			else
				sum -= stoi(num);
		}
	}
	
	cout << sum;

	return 0;
}
