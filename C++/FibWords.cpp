#include<iostream>
#include <unordered_map>
using namespace std;

void build(int trial, int x, unordered_map<int, string> &check);

int main() {
	int trial;
	string bit;
	int cases = 1;
	unordered_map<int, string> check;
	pair<int, string> zero (0, "0");
	pair<int, string> one (1, "1");
	check.insert(zero);
	check.insert(one);

	while (cin >> trial) {
		cin >> bit;
		unordered_map<int,string>::const_iterator got1 = check.find (trial);
		unordered_map<int,string>::const_iterator got2 = check.find (trial - 1);
		if (got1 != check.end()) {
			cout << "Case " << cases << ": " << got1->second << endl;
			cases++;
		}
		else if (got2 != check.end()) {
			string out = got2->second + check.at(trial - 2);
			pair<int, string> put (trial, out);
			check.insert(put);
			cout << "Case " << cases << ": " << out << endl;
			cases++;
		}
		else {
			int x = trial - 2;
			while (check.find(x) == check.end()) {
				x--;
			}
			build(trial, x, check);
			cout << "Case " << cases << ": " << check.at(trial) << endl;
			cases++;
		}
	}
}

void build(int trial, int x, unordered_map<int, string> &check) {
	while (x < trial) {
		x++;
		string out = check.at(x - 1) + check.at(x - 2);
		pair<int, string> put (x, out);
		check.insert(put);
	}
}