#include<iostream>
using namespace std;

int factors(int number);

int main() {
	int number;
	int check;
	while (cin >> number) {
		check = factors(number);
		if (check == number) {
			cout << number << " perfect" << endl;
    	}
    	else if (number - check <= 2) {
    		cout << number << " almost perfect" << endl;
    	}
    	else {
    		cout << number << " not perfect" << endl;
    	}
	}
}

int factors(int number) {
	int sum = 1;
      for (int x = 2; x < number; x++) {
         if (number%x == 0) {
            sum += x;
         }
      }
      return sum;
}
