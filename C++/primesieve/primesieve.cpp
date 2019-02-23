/*
Rating: ~ 5.5 / 10
Link: https://open.kattis.com/problems/primesieve
*/

#include <iostream>
#include <string>
#include <vector>
#include <bitset>
using namespace std;

int main() {
  int limit = 0;
  int q = 0;
  cin >> limit;
  cin >> q;
  static bitset<100000001> primes;
  primes.set(1);
  for (int p = 2; p * p <= limit; p++) {
    if (primes[p] != 1) {
      for (int i = p*p; i<=limit; i+= p) {
        primes.set(i);
      }
    }
  }
  int track = 0;
  for (int x = 1; x < limit+1; x++) {
    if (primes[x] == 0) {
      track++;
    }
  }
  cout << track << endl;
  for (int y = 0; y < q; y++) {
    int here;
    cin >> here;
    if (primes[here] == 0) {
      cout << 1 << endl;
    }
    else {
      cout << 0 << endl;
    }
  }

  return 0;
}
