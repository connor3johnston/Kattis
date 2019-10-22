/*
Rating: ~ 1.7 / 10
Link: https://open.kattis.com/problems/veci
*/

#include<iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	string line;
	cin >> line;
	int min = stoi(line);
	int track = min;
	if (next_permutation(line.begin(), line.end())) {
		cout << line << endl;
	}
	else {
		cout << 0 << endl;
	}
}
