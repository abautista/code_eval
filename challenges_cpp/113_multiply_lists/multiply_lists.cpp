//
// Created by Alberto Bautista  on 11/07/15.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

void multiply(string line) {
  string s1 = line.substr(0, line.find("|"));
  string s2 = line.substr(line.find("|") + 2);

  string word;

  stringstream ss1(s1);
  vector<int> v1;
  while (getline(ss1, word, ' ')) {
    v1.push_back(atoi(word.c_str()));
  }

  stringstream ss2(s2);
  vector<int> v2;
  while (getline(ss2, word, ' ')) {
    v2.push_back(atoi(word.c_str()));
  }

  for (int i = 0; i < v1.size(); i++) {
    cout << v1[i] * v2[i] << " ";
  }
}

int main(int argc, char *argv[]) {
  ifstream ifs(argv[1]);
  string line;

  while (getline(ifs, line)) {
    multiply(line);
    cout << endl;
  }
}