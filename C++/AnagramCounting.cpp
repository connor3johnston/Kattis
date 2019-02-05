#include<iostream>
#include<iterator>
#include<unordered_map>
using namespace std;
	long double factorial(long double val);

int main() {
	cout.setf(ios::fixed);
    cout.precision(0);
	string next = "";
	while (cin >> next) {
		unordered_map<char, long double> check;
		for (int x = 0; x < next.length(); x++) {
			char here = next.at(x);
			unordered_map<char, long double>::iterator the = check.find(here);
			if (the == check.end()) {
				pair<char, long double> that (here, 1);
				check.insert(that);
			}
			else {
				long double add = check[here] + 1;
				the->second = add;
			}
		}
		long double combos = factorial(next.length());
		unordered_map<char, long double>::iterator it;
		for(it = check.begin(); it != check.end(); it++) {
    		long double val = it->second;
    		if (val > 1) {
    			combos = combos / factorial(val);
    		}
		}	
		cout << combos << endl;
	}
}
	long double factorial(long double val) {
	long double out = 1;
	while (val > 1) {
		out *= val;
		val--;
	}
	return out;
}