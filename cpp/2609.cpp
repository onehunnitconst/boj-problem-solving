#include <iostream>

using namespace std;

void input (int* i) {
  cin >> *i;
}

void print (int o) {
  cout << o << '\n';
}

int euclidean(int n, int m) {
  int q = n;
  int r = m;

  while(r > 0) {
    int temp = q;
    q = r;
    r = temp % r;
  }

  return q;
}

int gcd(int n, int m) {
  return n < m ? euclidean(m, n) : euclidean(n, m);
}

int lcm(int n, int m) {
  return (n * m) / gcd(n, m);
} 

int main() {
  int n, m;

  input(&n);
  input(&m);

  print(gcd(n, m));
  print(lcm(n, m));

  return 0;
}