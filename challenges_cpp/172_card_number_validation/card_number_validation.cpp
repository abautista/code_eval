#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;


void check_card(string card_number)
{
  int result = 0;
  for (int i = card_number.size() - 1, j = 1; i >= 0; i--) {
    if (card_number[i] == ' ')
      continue;

    int number = card_number[i] - '0';
    if (j++ % 2 == 0) {
      number = number * 2;
      if (number > 9) {
        number = number / 10 + number % 10;
      }
    }
    result += number;
  }

  if (result % 10 == 0) {
    cout << "1" << endl;
  } else {
    cout << "0" << endl;
  }

}

int main(int argc, char *argv[])
{
  ifstream ifs(argv[1]);
  string line;

  while (getline(ifs, line)) {
    check_card(line);
  }
}
