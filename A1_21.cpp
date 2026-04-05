#include <iostream>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int year;

int main() {
    phuthitj;
    cin >> year;
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0) || (year % 15 == 0)) {
        cout << "yes";
    } else {
        cout << "no";
    }
    
    return 0;
}