#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <cstdlib>

using namespace std;

void the_major_element(string line)
{
  stringstream tokens(line);
  string token;
  vector<int> numbers;
  map<int, int> freqs;
  map<int, int>::iterator it;

  while (getline(tokens, token, ',')) {
    int number = atoi(token.c_str());
    numbers.push_back(number);
    it = freqs.find(number);

    if (it == freqs.end()) {
      freqs[number] = 1;
    } else {
      freqs[number] = freqs[number] + 1;
    }
  }
  int numbers_s_condition = numbers.size() / 2;
  for (it = freqs.begin(); it != freqs.end(); it++) {
    if (it->second > numbers_s_condition) {
      cout << it->first << endl;
      return;
    }
  }
  cout << "None" << endl;
}

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;

  while(getline(ifs, line)) {
    the_major_element(line);
  }
}
