#include <stdio.h>

#define MAXLINE 100

void fizz_buzz(int X, int Y, int N)
{
  int i;  
  for (i = 1; i <= N; i++) {
    if (i%X==0 && i%Y==0) {
      printf("FB");
    } else if (i%X==0) {
      printf("F");
    } else if (i%Y==0) {
      printf("B");
    } else {
      printf("%d", i);
    }
    if (i<N) printf(" ");
  }
  printf("\n");
}

int main(int argc, char *argv[])
{
  char line[MAXLINE];
  FILE *fp = fopen(argv[1], "r");
  int X, Y, N;
  
  while (fgets(line, sizeof(line), fp)) {
    sscanf(line, "%d%d%d", &X, &Y, &N);
    fizz_buzz(X, Y, N);
  }
  return 0;
}
