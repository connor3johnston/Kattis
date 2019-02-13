/*
Rating: ~ 3.6 / 10
Link: https://open.kattis.com/problems/meowfactor
*/

#include<iostream>
#include <math.h>
using namespace std;

int main() {
    long long int here;
    cin >> here;
    long long int check = 128;
    while (check > 1) {
        long long int copy = here;
        bool um = false;
        for (int x = 0; x < 9; x++) {
            if (copy%check == 0) {
                copy /= check;
            }
            else {
                break;
            }
            if (x == 8) {
                um = true;
            }
        }
        if (um) {
            break;
        }
        check--;
    }
    cout << check << endl;
}
