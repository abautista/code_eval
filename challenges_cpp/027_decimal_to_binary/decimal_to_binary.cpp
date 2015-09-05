#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <string>

using namespace std;

void decimal_to_binary(string line)
{
  int number = atoi(line.c_str());
  string binary;

  if (number == 0) {
    cout << 0 << endl;
    return;
  }

  while (number != 0) {
    int remainder = number % 2;
    number = number / 2;
    binary.push_back(remainder + '0');
  }
  reverse(binary.begin(), binary.end());
  cout << binary << endl;
}

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;
  while (getline(ifs, line)) {
    decimal_to_binary(line);
  }
}
