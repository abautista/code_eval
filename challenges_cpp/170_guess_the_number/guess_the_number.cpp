#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <cmath>

using namespace std;

void guess_number(string line)
{
  float low, high;
  stringstream ss(line);
  string tmp;
  
  getline(ss, tmp, ' ');
  low = 0;
  high = atof(tmp.c_str());
  
  while (getline(ss, tmp, ' ')) {
    float mid = (low + high) / 2;
    if (tmp == "Lower") {
      high = ceil(mid) - 1;
    } else if (tmp == "Higher") {
      low = ceil(mid) + 1;
    } else if (tmp == "Yay!") {
      cout << ceil(mid)  << endl;
      break;
    }
  }
}

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;

  while (getline(ifs, line)) {
    guess_number(line);
  }
}
