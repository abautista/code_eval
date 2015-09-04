#include <iostream>
#include <fstream>
#import <cctype>

using namespace std;

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;

  while (getline(ifs, line)) {
    int j = 0;
    for (int i = 0; i < line.size(); i++) {
      if (j % 2 == 0) {
        line[i] = toupper(line[i]);
      } else {
        line[i] = tolower(line[i]);
      }
      if (isalpha(line[i])) {
        j += 1;
      }
    }

    cout << line << endl;
  }
  return 0;
}
