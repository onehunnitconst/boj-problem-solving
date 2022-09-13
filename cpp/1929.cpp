#include <iostream>
#include <vector>

void print(int output)
{
  std::cout << output << '\n';
}

void input(int *m, int *n)
{
  std::cin >> *m >> *n;
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
  int m, n;

  input(&m, &n);

  for (int i = m; i <= n; i++)
  {
    if (isPrimeNumber(i))
    {
      print(i);
    }
  }
  return 0;
}