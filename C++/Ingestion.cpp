#include<iostream>
using namespace std;

void remove(int courses[], int meals);
int cals(int courses[], int calories, int meals);

int main() {
	int meals;
	int calories;
	cin >> meals;
	cin >> calories;
	int courses[meals];

	for (int x = 0; x < meals; x++) {
		cin >> courses[x];
	}
	int max = 0;
	for (int y = 0; y < meals; y++) {
		int check = cals(courses, calories, meals);
		if (check > max) {
			max = check;
		}
		remove(courses, meals);
	}
	cout << max << endl;
}

void remove(int courses[], int meals) {
	int index = 0;
	int check = 0;
	int min = courses[index];
	while (index < meals) {
		if (courses[index] < min) {
			min = courses[index];
			check = index;
		}
		index++;
	}
	courses[check] = 0;
}

int cals(int courses[], int calories, int meals) {
	int copy = calories;
	double rate = 2.0/3;
	double reverse = 3.0/2;
	int total = 0;
	for (int x = 0; x < meals; x++) {
		if (courses[x] == 0) {
			copy *= reverse;
		}
		else if (courses[x] > copy) {
			total += copy;
			copy *= rate;
		}
		else {
			total += courses[x];
			copy *= rate;
		}
	}
	return total;
}
