#include <iostream>
using namespace std;

int main() {
   int numberOfStones;

   cin >> numberOfStones;

   while (numberOfStones > 1) {
      numberOfStones -= 2;
   }
   
   if (numberOfStones == 1) {
      cout << "Alice" << endl;
   }
   else {
      cout << "Bob" << endl;
   }
}