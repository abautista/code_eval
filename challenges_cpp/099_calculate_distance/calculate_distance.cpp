#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>

using namespace std;

class Point {
public:
  int x, y;
  double distance(Point p);
};

double Point::distance(Point p)
{
  return sqrt(pow(abs(x - p.x), 2) + pow(abs(y - p.y), 2));
}

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;
  Point a, b;

  while (getline(ifs, line)) {
    sscanf(line.c_str(), "(%d, %d) (%d, %d)", &a.x, &a.y, &b.x, &b.y);
    cout << a.distance(b) << endl;
  }
}
