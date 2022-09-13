#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;
vector<int> arr;
vector<int> values;

int search(int value){
  int first = 0;
  int last  = arr.size() - 1;

  while (first <= last){
    int mid = (first + last) / 2;
    if(value > arr[mid]) {
      first = mid + 1;
    } else if (value < arr[mid]) {
      last = mid - 1;
    } else {
      return 1;
    }
  }

  return 0;
}

int main() {
  cin >> n;

  for (int i = 0; i < n; i++) {
    int element;
    cin >> element;
    arr.push_back(element);
  }

  cin >> m;

  for (int i = 0; i < m; i++) {
    int value;
    cin >> value;
    values.push_back(value);
  }

  sort(arr.begin(), arr.end());

  for (vector<int>::iterator it = values.begin(); it != values.end(); it++) {
    cout << search(*it) << '\n';
  }
  
  return 0;
}