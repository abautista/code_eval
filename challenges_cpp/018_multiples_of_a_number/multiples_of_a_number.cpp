#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;
  while (getline(ifs, line)) {
    int position = line.find_first_of(',');
    int first_number = atoi(line.substr(0, position).c_str());
    int second_number = atoi(line.substr(position + 1, line.size() - 1).c_str());

    int i = 2, multiple = second_number;
    while (first_number > multiple) {
      multiple = second_number * i++;
    }
    cout << multiple << endl;
  }

}
