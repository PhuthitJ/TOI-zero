#include <iostream>
#include <string>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int main() {
    phuthitj;
    int price;
    int age;
    string dayinweek;
    cin >> age >> dayinweek;
    if (age < 5) {
        price = 0;
    } else if (age > 18) {
        price = 150;
    } else {
        price = 100;
    }

    if (dayinweek == "Wed") {
        price = price / 2;
    }

    cout << price << endl;

    return 0;
}