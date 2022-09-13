#include <iostream>
#include <vector>

void print(int output)
{
  std::cout << output << '\n';
}

void input(int* input)
{
  std::cin >> *input;
}

bool isPrimeNumber(int num)
{
  bool result = true;

  if (num == 1) result = false;

  for (int i = 2; i*i <= num; i++) {
    if (num % i == 0) {
      result = false;
    }
  }

  return result;
}

int main(int argc, char const *argv[])
{
  int n, count = 0;

  input(&n);

  for (int i = 0; i < n; i++)
  {
    int m;

    input(&m);

    if (isPrimeNumber(m))
    {
      count++;
    }
  }

  print(count);

  return 0;
}