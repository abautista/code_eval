#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;
  while (getline(ifs, line)) {
    int number = atoi(line.c_str());
    (number % 2 == 0)? cout << 1 : cout << 0;
    cout << endl;
  }
}
