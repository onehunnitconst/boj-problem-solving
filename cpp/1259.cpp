#include <iostream>
#include <string>

bool isPalindromeInteger(std::string integer) {
  int length = integer.length();
  for (int i=0; i<length/2; i++) {
    if (integer[i] != integer[length - (i + 1)]) {
      return false;
    }
  }
  return true;
}

int main(int argc, char const *argv[])
{
  std::string integer;

  while (true) {
    std::cin >> integer;
    if (integer == "0") break;

    std::string message = isPalindromeInteger(integer) ? "yes\n": "no\n";
    std::cout << message;
  }

  return 0;
}
