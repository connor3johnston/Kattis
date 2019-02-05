#include<iostream>
#include<unordered_set>
using namespace std;

int main() {
	int size = 0;
	int changes, broken;
	cin >> size >> changes >> broken;
	unordered_set<int> set;
	for (int x = 0; x < broken; x++) {
		int next;
		cin >> next;
		set.insert(next);
	}
	int last = 0;
	int out[size];
	for (int z = 0; z < size; z++) {
		out[z] = 0;
	}
	if (changes%2==1) {
		changes--;
		out[0] = 1;
		last = 1;	
	}
	int index = 1;
	while (index < size && changes > 0) {
		if (set.find(index+1) == set.end() && last != 1) {
			out[index] = 1;
			last = 1;
			changes -= 2;
		}
		else {
			last = 0;
		}
		index++;
	}
	for (int y = 0; y < size; y++) {
		cout << out[y];
	}
	cout << endl;
}
