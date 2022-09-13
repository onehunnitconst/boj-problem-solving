#include <iostream>
#include <string>

using namespace std;

void input (int* i) {
  cin >> *i;
}

void print (int o) {
  cout << o << '\n';
}

bool isConstructor(int n, int m) {
  int sum = m;
  string str = to_string(m);

  for(int i=0; i<str.length(); i++) {
    sum += str[i] - '0';
  }
  
  return n == sum;
}

int main() {
  int n;
  int con = 0;

  input(&n);

  int range = n>54 ? n-54 : 0;

  for (int i=range; i<=n; i++) {
    if (isConstructor(n, i)) {
      con = i;
      break;
    }
  }

  print(con);

  return 0;
}