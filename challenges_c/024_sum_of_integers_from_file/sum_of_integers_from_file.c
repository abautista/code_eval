#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int sum = 0;
  FILE *fp = fopen(argv[1], "r");
  char line[256];

  while (fgets(line, 256, fp)) {
    sum += atoi(line);
  }
  printf("%d\n", sum);
  return 0;
}
