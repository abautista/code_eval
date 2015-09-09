#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>

using namespace std;

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;

  while (getline(ifs, line)) {
    int O, P, Q, R;
    sscanf(line.c_str(), "%d %d %d %d", &O, &P, &Q, &R);

    if (O == Q && P == R) {
      cout << "here" << endl;

    } else if (O == Q && R > P) {
      cout << "N" << endl;

    } else if (O == Q && R < P) {
      cout << "S" << endl;

    } else if (P == R && Q > O) {
      cout << "E" << endl;

    } else if (P == R && Q < O) {
      cout << "W" << endl;

    } else if (Q > O && R > P) {
      cout << "NE" << endl;

    } else if (Q > O && R < P) {
      cout << "SE" << endl;

    } else if (Q < O && R > P) {
      cout << "NW" << endl;

    } else if (Q < O && R < P) {
      cout << "SW" << endl;
    }
  }
  return 0;
}
