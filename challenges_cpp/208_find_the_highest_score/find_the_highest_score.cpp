#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <stdlib.h>
#include <vector>

using namespace std;

void find_highest_score(string line)
{
  stringstream ss(line);
  string row;
  vector<int> highest_scores;
  int i = 0;

  while(getline(ss, row, '|')) {

    int pos = row.find_first_not_of(' ');
    row = row.substr(pos);

    stringstream ssrow(row);
    string token;
    int j = 0;
    while (getline(ssrow, token, ' ')) {
      int number = atoi(token.c_str());
      if (i == 0) {
        highest_scores.push_back(number);
      } else {
        if (highest_scores[j] < number) {
          highest_scores[j] = number;
        }
      }
      j++;
    }
    i++;
  }

  vector<int>::iterator it;
  for (it = highest_scores.begin(); it != highest_scores.end(); it++) {
    cout << *it << " ";
  }
  cout << endl;

}

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;

  while(getline(ifs, line)) {
    find_highest_score(line);
  }
}
