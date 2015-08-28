#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;

  while (getline(ifs, line)) {
    int pos = line.find_first_of(',');
    string sub1 = line.substr(0, pos);
    string sub2 = line.substr(pos+1);

    string::reverse_iterator rit;
    int i = sub1.size() - 1;
    for (rit = sub1.rbegin(); rit != sub1.rend(); rit++) {
      if (*rit == sub2[0]) {
        break;
      }
      i--;
    }
    if (rit == sub1.rend()) {
      cout << -1 << endl;
    } else {
      cout << i << endl;
    }
  }
}
