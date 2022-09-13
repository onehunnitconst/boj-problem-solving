#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

void print(int output)
{
  std::cout << output << '\n';
}

void input(int* input)
{
  std::cin >> *input;
}

int mean(int* arr, int n) {
  double total = 0.0f;
  double offset = 0.5;

  for(int i = 0; i < n; i++) {
    total += arr[i];
  }

  return floor(total / n + offset);
}

int median(int* arr, int n) {
  return arr[(n-1)/2];
}

int range(int* arr, int n) {
  return arr[n-1] - arr[0];
}

int mode(int* arr, int n) {
  int* index = new int[range(arr, n) + 1]();
  int offset = arr[0];
  std::vector<int> modes;
  int maxCount = 0;

  for(int i = 0; i < n; i++) {
    index[arr[i] - offset]++;
  }

  for(int i = 0; i < range(arr, n) + 1; i++) {
    if (index[i] > maxCount) {
      maxCount = index[i];
    }
  }

  for(int i = 0; i < range(arr, n) + 1; i++) {
    if (index[i] == maxCount) {
      modes.push_back(i + offset);
    }
  }

  return modes.size() > 1 ? modes[1] : modes[0];
}

int main(int argc, char const *argv[])
{
  int n;

  input(&n);

  int* arr = new int[n];

  for(int i = 0; i < n; i++) {
    input(&arr[i]);
  }

  std::sort(arr, arr+n);

  print(mean(arr, n));
  print(median(arr, n));
  print(mode(arr, n));
  print(range(arr, n));

  return 0;
}