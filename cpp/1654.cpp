#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int k, n;
vector<int> cables;
unsigned int min_len = 1;
unsigned int max_len = 0;

int search() {
  unsigned int result = 0;

  while(min_len <= max_len){
    int cn = 0;
    unsigned int mid = (min_len + max_len) / 2;
    for (vector<int>::iterator it = cables.begin(); it != cables.end(); ++it) {
      cn += *it / mid;
    }

    if (cn < n){
      max_len = mid - 1;
    } else if (cn >= n) {
      min_len = mid + 1;
    }

    result = max_len;
  }

  return result;
}

int main(){  
  cin >> k >> n;

  for(int i=0; i<k; i++){
    unsigned int len;
    cin >> len;
    max_len = max(max_len, len);
    cables.push_back(len);
  }

  cout << search() << '\n';

  return 0;
}