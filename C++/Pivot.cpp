#include <iostream>
#include <algorithm>    
using namespace std;

int main() {
   int numbers;
   cin >> numbers;
   int a[numbers];
   for (int x = 0; x < numbers; x++) {
      cin >> a[x];
   }
   int count = 0;
   for (int y = 0; y < numbers; y++) {
      for (int z = 0; z < numbers; z++) {
         if ((y != 0 && y != numbers - 1 && z != 0 && z != z-1) && y == z) {
            continue;;
         }
         else if (z < y && a[z] > a[y]) {
            break;
         }
         else if (z > y && a[z] <= a[y]) {
            break;
         }
         if (z + 1 == numbers) {
            count++;
         }
      }
   }
   cout << count << endl;
}
