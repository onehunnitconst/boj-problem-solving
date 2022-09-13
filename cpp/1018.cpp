#include <iostream>
#include <cmath>

char inputBoard[51][51];

int n, m;

int count(int roffset, int coffset) {
  int countA = 0;
  int countB = 0;
  char first = inputBoard[roffset][coffset];

  for(int index = roffset; index < roffset + 8; index++) {
    for(int subIndex = coffset; subIndex < coffset + 8; subIndex++) {
      if (index % 2 == 0) {
        if (subIndex % 2 == 0) {
          if (inputBoard[index][subIndex] != first) countA++;
          else countB++;
        } else {
          if (inputBoard[index][subIndex] == first) countA++;
          else countB++;
        }
      } else {
        if (subIndex % 2 == 0) {
          if (inputBoard[index][subIndex] == first) countA++;
          else countB++;
        } else {
          if (inputBoard[index][subIndex] != first) countA++;
          else countB++;
        }
      }
    }
  }

  return fminl(countA, countB);
}

int main() {
  std::cin >> n >> m;
  int result = 64;

  for(int index = 0; index < n; index++) {
    for(int subIndex = 0; subIndex < m; subIndex++) {
      std::cin >> inputBoard[index][subIndex];
    }
  }

  for(int index = 0; index < n - 8 + 1; index++) {
    for(int subIndex = 0; subIndex < m - 8 + 1; subIndex++) {
      result = fminl(result, count(index, subIndex));
    }
  }

  std::cout << result;

  return 0;
}