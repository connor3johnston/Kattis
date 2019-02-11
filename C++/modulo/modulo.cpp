/*
Rating: ~ 2.4 / 10
Link: https://open.kattis.com/problems/modulo
*/

#include<iostream>
#include<unordered_set>

using namespace std;

int main() {
	unordered_set<int> set;
	int count = 0;
	int next;
	while (count < 10) {
		cin >> next;
		set.insert(next%42);
		count++;
	}
	cout << set.size() << endl;
}
