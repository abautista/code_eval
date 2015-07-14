#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <iomanip>

using namespace std;

void processLine(string line) {
  stringstream ss(line);
  vector<double> v;
  string word;
  
  while (getline(ss, word, ' ')) {
    v.push_back(atof(word.c_str()));
  }
  sort(v.begin(), v.end());

  vector<double>::iterator iter;
  for (iter = v.begin(); iter != v.end(); ++iter) {
    cout << fixed << setprecision(3) << *iter << " ";
  }
  cout << endl;
}

int main(int argc, char *argv[]) {
  ifstream iss(argv[1]);
  string line;
  while (getline(iss, line)) {
    processLine(line);
  }
}
