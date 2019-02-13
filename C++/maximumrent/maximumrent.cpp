/*
Rating: ~ 2.8 / 10
Link: https://open.kattis.com/problems/maximumrent
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	int rentFoot;
	int rentBulb;
	int maxThings;
	int outlets;
	cin >> rentFoot;
	cin >> rentBulb;
	cin >> maxThings;
	cin >> outlets;

	int fts = maxThings/2;
	int bulbs = maxThings - fts;
	int rent = 0;

	while(bulbs > 0) {
		int track;
		track = 2*fts+bulbs;
		if(track < outlets) {
			break;
		}
		int tryRent;
		tryRent = rentFoot * fts  + rentBulb * bulbs;
        if (tryRent > rent) {
            rent = tryRent;
        }
        bulbs--;
        fts++;
    }
    bulbs = maxThings/2;
    fts = maxThings - bulbs;
    while (fts > 0) {
        int track = 2 * fts + bulbs;
        if (track < outlets) {
            break;
        }
        int tryRent = rentFoot * fts  + rentBulb * bulbs;
        if (tryRent > rent) {
           rent = tryRent;
        }
        fts--;
        bulbs++;
    }
    cout << rent << endl;
}
