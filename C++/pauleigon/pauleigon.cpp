/*
Rating: ~ 1.6 / 10
Link: https://open.kattis.com/problems/pauleigon
*/

#include<iostream>

using namespace std;

int main() {
	int serves;
	int score1;
	int score2;

	cin >> serves >> score1 >> score2;
	if ((score1+score2)/serves%2 == 0) {
		cout << "paul" << endl;
	}
	else {
		cout << "opponent" << endl;
	}
}
