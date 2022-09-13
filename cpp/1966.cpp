#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void input (int* i) {
  cin >> *i;
}

void print (int o) {
  cout << o << '\n';
}

int main() {
  int t;

  input(&t);

  for(int tc = 0; tc < t; tc++) {
    int n, m;
    int current_queue = 0;
    int current_order = m;
    vector<int> printer_queue;
    vector<int> sorted_priority;

    input(&n);
    input(&m);

    for(int i=0; i<n; i++) {
      int doc;
      input(&doc);
      printer_queue(doc);
      sorted_priority(doc);
    }

    sort(sorted_priority.begin(), sorted_priority.end(), greater<int>());

    while(printer_queue.size() > 1) {
      if (printer_queue.front() == sorted_priority.front()) {
        printer_queue.erase(printer_queue.begin());
        sorted_priority.erase(sorted_priority.begin());
        current_queue++;
        
      }
    }


  }

  return 0;
}