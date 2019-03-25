/*
Rating: ~ 4.3 / 10
Link: https://open.kattis.com/problems/unionfind
*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;

//Global variables
vector<int> parents;

//Helper functions
void unionwith(int L, int R);
void build(int N);
int find(int I);

void fast() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
}

int main() {
  fast();
  int N, Q;
  cin >> N >> Q;
  build(N);
  for (int x = 0; x < Q; x++) {
    char mark;
    int L, R;
    cin >> mark >> L >> R;
    if (mark == '?') {
      if (find(L) == find(R)) {
        cout << "yes" << endl;
      }
      else {
        cout << "no" << endl;
      }
    }
    else {
      unionwith(L, R);
    }
  }


  return 0;
}

void unionwith(int L, int R) {
  parents[find(R)] = find(L);
}

void build(int N) {
  for (int x = 0; x < N; x++) {
    parents.push_back(x);
  }
}

int find(int I) {
  if (parents[I] == I) {
    return I;
  }
  parents[I] = find(parents[I]);
  return parents[I];
}
