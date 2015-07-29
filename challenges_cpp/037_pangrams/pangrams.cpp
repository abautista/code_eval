#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

using namespace std;

int main(int argc, char *argv[])
{
  string line;
  int position;
  ifstream ifs(argv[1]);  
  string::iterator it;
  
  while (getline(ifs, line)) {
    bool empty = true;      
    bool characters[26] = {false};
    
    for (it=line.begin(); it!=line.end(); it++) {
      if (isalpha(*it)) {
	position = tolower(*it) - 'a';
	characters[position] = true;
      }
    }

    for (int i=0; i<26; i++) {
      if (characters[i]==false) {
	empty = false;
	cout << static_cast<char>('a' + i);
      }
    }

    if (empty) cout << "NULL";
    cout << endl;    
  }
  
}
