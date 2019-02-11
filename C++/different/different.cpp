/*
Rating: ~ 2.1 / 10
Link: https://open.kattis.com/problems/acm2
*/

#include <iostream>
using namespace std;

int main() {
   long a;
   long b;

   while (cin >> a) {
      cin >> b;
      cout << abs(b - a) << endl;
   }
}
