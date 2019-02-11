/*
Rating: ~ 2.7 / 10
Link: https://open.kattis.com/problems/candlebox
*/

#include<iostream>
using namespace std;

int main() {
	int dif;
	int rita;
	int theo;
	cin >> dif;
	cin >> rita;
	cin >> theo;
	int ritaAge = 4;
	int theoAge = ritaAge - dif;
	int candlesR = 0;
	int candlesT = 0;
	while (candlesR + candlesT != theo + rita) {
		candlesR += ritaAge;
		if (theoAge > 2) {
			candlesT += theoAge;
		}
		ritaAge++;
		theoAge++;
	}
	int output = rita - candlesR;
	cout << output << endl;
}
