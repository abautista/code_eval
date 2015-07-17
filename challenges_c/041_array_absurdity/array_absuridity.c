#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINE 256

void array_absurdity(char *line)
{
  char *token;
  int tokens_number;
  int i, number;
  
  token = strtok(line, ";\n");
  tokens_number = atoi(token);

  int numbers[tokens_number];
  for (i = 0; i<tokens_number-1; i++) {
    numbers[i] = i;
  }

  for (i=0; i<tokens_number; i++) {
    number = atoi(strtok(NULL, ",\n"));
    if (numbers[number] == -1) {
      printf("%d\n", number);
      break;
    } else {
      numbers[number] = -1;
    }
  }
  
}

int main(int argc, char *argv[])
{
  FILE *fp = fopen(argv[1], "r");
  char line[MAXLINE];

  while (fgets(line, sizeof(line), fp)) {
    array_absurdity(line);
  }
  
  return 0;
}
