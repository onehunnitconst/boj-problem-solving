#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int n;
std::vector<std::string> words;

bool compWords(std::string first, std::string second) {
  int firstLength = first.length();
  int secondLength = second.length();

  if (firstLength == secondLength) {
    for (int i=0; i<firstLength; i++) {
      if (first[i] != second[i]) {
        return first[i] < second[i];
      }
    }
  }
  
  return firstLength < secondLength;
}

void sortWords() {
  sort(words.begin(), words.end(), compWords);
  words.erase(unique(words.begin(), words.end()), words.end());
}

int main(int argc, char *argv[]) {
  
  std::cin >> n;

  for(int i=0; i<n; i++) {
    std::string str;
    std::cin >> str;
    words.push_back(str);
  }

  sortWords();

  for(int i=0; i<words.size(); i++) {
    std::cout << words[i] << '\n';
  }

  return 0;
}