#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
  ifstream istream(argv[1]);
  string line;
  vector<string> words;
  
  while (getline(istream, line)) {
    words.clear();
    stringstream ss(line);
    string word;
    while (ss >> word) {
      words.push_back(word);
    }

    vector<string>::reverse_iterator ri;
    for (ri = words.rbegin(); ri != words.rend(); ri++) {
      if (ri != words.rbegin()) {
	cout << " ";
      }
      cout << *ri;
    }
    cout << endl;
  }
}
