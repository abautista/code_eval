#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#define MAXLINE 1000

using namespace std;

int main(int argc, char *argv[])
{
  FILE *fp = fopen(argv[1], "r");
  char line[MAXLINE];
  vector<int> numbers;
  vector<int> checkedNumbers;
  bool isJolly;
  char *token;
  
  while(fgets(line, sizeof(line), fp)) {
    isJolly = true;
    numbers.clear();
    checkedNumbers.clear();
    
    token = strtok(line, " ");
    while (token!=NULL) {
      numbers.push_back(atoi(token));
      token = strtok(NULL, " ");
    }
    
    if (numbers.size()==1) {
      printf("Jolly\n");
  
    } else {
      
      for (unsigned int i=0; i<numbers.size()-2; i++) {
	checkedNumbers.push_back(false);
      }
    
      for (unsigned int i=0; i<numbers.size()-1; i++) {	
	unsigned int d = abs(numbers[i]-numbers[i+1]);	
	if (d>=1 && d<=numbers.size()) {
	  checkedNumbers[d-1] = true;
	}      
      }

      for (unsigned int i=0; i<checkedNumbers.size(); i++) {
	if (checkedNumbers[i]==false) {	
	  isJolly = false;
	  break;
	}
      }

      if (isJolly==true) {
	printf("Jolly\n");
      } else {
	printf("Not jolly\n");
      }
    }
  }
  return 0;
}

