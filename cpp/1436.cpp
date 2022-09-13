#include <iostream>
#include <string>

using namespace std;

int main() {
  int n;
  cin >> n;

  int index = 0;
  int title = 0;

  while (index < n) {
    title++;
    if (to_string(title).find("666") != string::npos) {
      index++;
    }
  }

  cout << title << '\n';
  
  return 0;
}