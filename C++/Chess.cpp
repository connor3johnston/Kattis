#include<iostream>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	bool board[8][8];
	for (int a = 0; a < 8; a++) {
		for (int b = 0; b < 8; b++) {
			if (a%2 == 0 && b%2==1) {
				board[a][b] = true;
			}
			else if (a%2==1 && b%2==0) {
				board[a][b] = true;
			}
		}
	}
	for (int x = 0; x < cases; x++) {
		char col1;
		char col2;
		int row1;
		int row2;
		cin >> col1 >> row1 >> col2 >> row2;
		int c1 = col1 - 65;
		int c2 = col2 - 65;
		if (board[row1][c1] != board[row2][c2]) {
			cout << "impossible" << endl;
			continue;
		}
		if (row1 == row2 && col1 == col2) {
			cout << "0 " << col1 << " " << row1 << endl;
			continue;
		}
		int slope = abs((row1-row2)/(c1-c2));
		if (slope == 1) {
			cout << "1 " << col1 << " " << row1 << " " << col2 << " " << row2 << endl;
		}
		else {
			int newRow = (row1+row2)/2;
			int newCol = abs(newRow - row1);
			if (c1 <= c2) {
				newCol -= c1;
			}
			else {
				newCol += c1;
			}
			char newChar = newCol + 65;
			cout << "2 " << col1 << " " << row1 << " " << newChar << " " << newRow << " " << col2 << " " << row2 << endl;
		}			
	}
}
