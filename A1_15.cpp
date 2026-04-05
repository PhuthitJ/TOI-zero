#include <iostream>
#include <string>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int main() {
    phuthitj;
    string firstname, lastname;
    int age;
    cin >> firstname >> lastname >> age;
    int last_digit = age % 10;

    if (firstname.length() >= 6 && lastname.length() >= 6) {
        cout << firstname.substr(0,2) << lastname.back() << last_digit;
    } else {
        cout << firstname.substr(0,1) << age << lastname.back();
    }

    return 0;
}