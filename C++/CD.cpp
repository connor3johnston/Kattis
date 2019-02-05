#include<iostream>
#include<set>
using namespace std;

int main() {
   int next;
   int jack;
   int jill;
   int count;
   
   while (cin >> jack) {
      cin >> jill;
      if (jack == 0 && jill == 0) {
         break;
      }
      set<int> catalog;
      count = 0;
   
      for (int x = 0; x < jack; x++) {
         cin >> next;
         catalog.insert(next);
      }
   
      for (int y = 0; y < jill; y++) {
         cin >> next;
         if (catalog.count(next) == 1) {
            count++;
         }
      }
      cout << count << endl;
   }
}