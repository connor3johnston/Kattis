/*
Rating: ~ 2.9 / 10
Link: https://open.kattis.com/problems/anothercandies
*/

#include<iostream>
#include <string>
#include <stdio.h>
#include <math.h>
using namespace std;

int main() {
		string c;
		getline(cin, c);
		int cases = stoi(c);
		string blank;
		getline(cin, blank);
		for (int x = 0; x < cases; x++) {
			string k;
			getline(cin, k);
			int kids = stoi(k);
			long double total = 0;
			for (int y = 0; y < kids; y++) {
				string add;
				getline(cin, add);
				total += fmod(stold(add), kids);
			}
			if (fmod(total, kids) == 0) {
				cout << "YES" << endl;
			}
			else {
				cout << "NO" << endl;
			}
			getline(cin, blank);
		}
	}
