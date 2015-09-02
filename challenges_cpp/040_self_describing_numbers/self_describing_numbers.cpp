#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

void self_describing_numbers(string line)
{
  map<int, int> digits_dictionary;
  map<int, int>::iterator it;
  int key;

  for (int i = 0; i < 10; i++) {
    digits_dictionary[i] = 0;
  }

  for (int i = 0; i < line.size(); i++) {
    key = line[i] - '0';
    it = digits_dictionary.find(key);
    if (it != digits_dictionary.end()) {
      it->second = it->second + 1;
    }
  }

  for (int i = 0; i < line.size(); i++) {
    it = digits_dictionary.find(i);
    int value = line[i] - '0';
    if (it == digits_dictionary.end() || it->second != value) {
      cout << 0 << endl;
      return;
    }
  }
  cout << 1 << endl;
}

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;
  while (getline(ifs, line)) {
    self_describing_numbers(line);
  }
}
