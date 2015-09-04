#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

using namespace std;

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;
  while (getline(ifs, line)) {
    for (int i = 0; i < line.size(); i++) {
      if (islower(line[i])) {
        line[i] = toupper(line[i]);
      } else {
        line[i] = tolower(line[i]);
      }
    }
    cout << line << endl;
  }
}
