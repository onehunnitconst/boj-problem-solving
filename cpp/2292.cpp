#include <iostream>

using namespace std;

void input (int* i) {
  cin >> *i;
}

void print (int o) {
  cout << o << '\n';
}

int main() {
  int n;
  int rooms = 1;
  input(&n);

  while(n > 1) {
    n -= rooms * 6;
    rooms++;
  }

  print(rooms);

  return 0;
}