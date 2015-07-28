#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>

using namespace std;

int main(int argc, char *argv[])
{
  string line, str1, str2;
  ifstream ifs(argv[1]);

  while (getline(ifs, line)) {
    int pos1 = line.find_first_of(",");
    str1 = line.substr(0, pos1);
    str2 = line.substr(pos1+1, line.length()-1);
    
    for (int j=str2.length()-1, i=str1.length()-1; j>=0; j--, i--) {
      if (str1[i]!=str2[j]) {
	cout << "0" << endl;
	break;
      }
      
      if (j==0) {
	cout << "1" << endl;
      }      
    }
  }
  return 0;
}


