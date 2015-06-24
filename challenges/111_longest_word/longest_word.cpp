#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(int argc, char *argv[]) {
  
    ifstream stream(argv[1]);
    string line;
  
    while (getline(stream, line)) {
        stringstream iss(line);
    
        string word;
        string longest;
        while (iss >> word) {
            if (longest.length() < word.length()) {
                longest = word;
            }
        }
        cout << longest << endl;
    }
  return 0;
}
