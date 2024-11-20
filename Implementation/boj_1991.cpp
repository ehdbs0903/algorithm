#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

unordered_map <char, vector<char>> graph;

void preorder(char node) {
	if (node == '.') return;
	cout << node;
	preorder(graph[node][0]);
	preorder(graph[node][1]);
}

void inorder(char node) {
	if (node == '.') return;
	inorder(graph[node][0]);
	cout << node;
	inorder(graph[node][1]);
}

void postorder(char node) {
	if (node == '.') return;
	postorder(graph[node][0]);
	postorder(graph[node][1]);
	cout << node;
}

int main() {
	int n;

	cin >> n;

	for (int i = 0; i < n; i++) {
		char root, left, right;

		cin >> root >> left >> right;

		graph[root] = { left, right };
	}

	preorder('A');
	cout << "\n";
	inorder('A');
	cout << "\n";
	postorder('A');

	return 0;
}
