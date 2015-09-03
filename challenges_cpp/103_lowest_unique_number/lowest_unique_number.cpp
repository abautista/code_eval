#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;
  vector<int> all_numbers;
  set<int> numbers, repeated;

  while (getline(ifs, line)) {
    numbers.clear();
    repeated.clear();
    all_numbers.clear();

    stringstream tokens(line);
    string token;

    set<int>::iterator it_numbers, it_repeated;

    while (getline(tokens, token, ' ')) {
      int min_number, index_min_number;
      int number = atoi(token.c_str());

      it_numbers = numbers.find(number);
      it_repeated = repeated.find(number);
      all_numbers.push_back(number);

      if (it_numbers == numbers.end() && it_repeated == repeated.end()) {
        numbers.insert(number);
      } else if (it_numbers != numbers.end() && it_repeated == repeated.end()){
        repeated.insert(number);
        numbers.erase(it_numbers);
      }
    }

    int min_number = *min_element(numbers.begin(), numbers.end());
    vector<int>::iterator index = find(all_numbers.begin(), all_numbers.end(), min_number);
    if (index != all_numbers.end()) {
      cout << index - all_numbers.begin() + 1 << endl;
    } else {
      cout << 0 << endl;
    }
  }
}
