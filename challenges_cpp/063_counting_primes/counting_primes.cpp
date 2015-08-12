#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

void count_primes(int x, int y) {

  bool *sieve = new bool[y+1];
  int upper_limit = y + 1;
  int count = 0;

  for (int i = 0; i < upper_limit; i++) {
    sieve[i] = true;
  }
  
  for (int i = 2; i < y; i++) {
    for (int m = i + i; m < upper_limit; m = m + i) {
      sieve[m] = false;
    }
  }

  for (int i = x; i <= y; i++) {
    if (sieve[i] == true)
      count++;
  }

  cout << count << endl;
  
}

int main(int argc, char *argv[]) {
  int x, y;
  FILE *fp = fopen(argv[1], "r");
  char line[200];
  while (fgets(line, sizeof(line), fp)) {
    sscanf(line, "%d,%d", &x, &y);
    count_primes(x, y);
  }
  
}
