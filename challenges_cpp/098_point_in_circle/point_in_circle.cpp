#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef struct {
  float x, y;
} Point;

void point_in_circle(Point center, float radius, Point p)
{

  float d = sqrt(pow(p.x - center.x, 2) + pow(p.y - center.y, 2));
  if (d < radius) {
    cout << "true" << endl;
  } else {
    cout << "false" << endl;
  }
}

int main(int argc, char *argv[])
{
  Point center, point;
  float radius;
  ifstream ifs(argv[1]);
  string line;

  while (getline(ifs, line)) {
    sscanf(line.c_str(), "Center: (%f, %f); Radius: %f; Point: (%f, %f)", &center.x, &center.y, &radius, &point.x, &point.y);
    point_in_circle(center, radius, point);

  }
}
