#include <iostream>
#include <cmath>

int x, y, w, h;
int direction[4];

int minLengthFromEdge() {
  int minLength;

  direction[0] = x;
  direction[1] = y;
  direction[2] = w-x;
  direction[3] = h-y;

  minLength = direction[0];

  for (int i=1; i<4; i++) {
    minLength = fminl(minLength, direction[i]);
  }

  return minLength;
}

int main(int argc, char *argv[]) {
  std::cin >> x >> y >> w >> h;
  std::cout << minLengthFromEdge();
  return 0;
}