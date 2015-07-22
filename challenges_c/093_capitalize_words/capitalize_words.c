#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAXLINE 100

int main(int argc, char *argv[])
{
  char line[MAXLINE];
  
  FILE *fp = fopen(argv[1], "r");
  while (fgets(line, sizeof(line), fp)) {

    enum {
      WORD_INSIDE,
      WORD_OUTSIDE
    } state;

    int i = 0;
    int word_beginning = 0;
    state = WORD_OUTSIDE;
    
    while (line[i]!='\0') {
      if ((line[i]==' '|| line[i]=='\n' )&& state==WORD_INSIDE) {
	line[word_beginning] = toupper(line[word_beginning]);
	state = WORD_OUTSIDE;
	
      }  else if ((line[i]!=' '|| line[i]=='\n') && state==WORD_OUTSIDE) {
        word_beginning = i;
	state = WORD_INSIDE;
      }
      i++;
    }
    printf("%s", line);
  }
  return 0;
}
