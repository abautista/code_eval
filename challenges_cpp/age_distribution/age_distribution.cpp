#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    int age;
    ifstream ifs(argv[1]);

    while (ifs >> age) {
        if (0 <= age && age <= 2) {
            cout << "Still in Mama's arms" << endl;
        } else if (3 <= age && age <= 4) {
            cout << "Preeschool Maniac" << endl;
        } else if (5 <= age && age <= 11) {
            cout << "Elementary school" << endl;
        } else if (12 <= age && age <= 14) {
            cout << "Middle school" << endl;
        } else if (15 <= age && age <= 18) {
            cout << "High school" << endl;
        } else if (19 <= age && age <= 22) {
            cout << "College" << endl;
        } else if (23 <= age && age <= 65) {
            cout << "Working for the man" << endl;
        } else if (66 <= age && age <= 100) {
            cout << "The Golden Years" << endl;
        } else {
            cout << "This program is for humans" << endl;
        }
    }
    return 0;
}
