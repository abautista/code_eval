#include <iostream>

using namespace std;

bool isPrime(int number) {
  for (int i=2; i<number; i++) {
    if (number % i == 0) {
      return false;
    }
  }
  return true;
}

int main() {
  int count = 0;
  int sum = 0;
  
  int currentNumber = 2;
  while (count<1000) {
    if (isPrime(currentNumber)) {
      count++;
      sum += currentNumber;
    }
    currentNumber++;
  }

  cout << sum << endl;
}
