#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    int number;
    ifstream ifs(argv[1]);

    ifs >> hex;
    while (ifs >> number) {
        cout << number << endl;
    }
}
