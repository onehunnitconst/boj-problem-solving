#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

stack<int> stack_seq;
vector<int> seq;
vector<char> op;

int main(){
  int n;
  cin >> n;

  for (int i=0; i<n; i++) {
    int num;
    cin >> num;
    seq.push_back(num);
  }

  vector<int>::iterator it = seq.begin();

  for(int i = 1; i <= seq.size(); i++){
    stack_seq.push(i);
    op.push_back('+');

    while(!(stack_seq.empty()) && stack_seq.top() == *it){
      stack_seq.pop();
      op.push_back('-');
      ++it;
    }
  }

  if (stack_seq.empty()){
    for(vector<char>::iterator it = op.begin(); it != op.end(); it++){
      cout << *it << '\n';
    }
  } else {
    cout << "NO" << '\n';
  }

  return 0;
}