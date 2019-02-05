#include <iostream>
#include <math.h>
using namespace std;

int main() {

   cout.setf(ios::fixed);
   cout.setf(ios::showpoint);
   cout.precision(25); 
               
   double area;
   double side_length;

   cin >> area;
   side_length = sqrt(area);

   cout << side_length * 4 << endl;
}