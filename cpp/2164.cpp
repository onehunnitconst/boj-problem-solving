#include <iostream>
#include <queue>

using namespace std;

void input (int* i) {
  cin >> *i;
}

void print (int o) {
  cout << o << '\n';
}

int main() {
  int n;
  queue<int> cards;
  input(&n);

  for (int i=0; i<n/2; i++) {
    cards.push((i+1)*2);
  }
  
  if (n == 1) {
    print(1);
  } else {
    if (n % 2 != 0) {
      cards.push(cards.front());
      cards.pop();
    }
    while(cards.size() > 1) {
      cards.pop();
      cards.push(cards.front());
      cards.pop();
    }
    print(cards.front());
  }

  return 0;
}