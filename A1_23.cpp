#include <iostream>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int temp;
char unit;

int main() {
    phuthitj;
    cin >> temp >> unit;
    if (unit == 'C') { // Celsius
        if (temp < 0) cout << "solid\n";
        else if (temp < 100) cout << "liquid\n";
        else cout << "gas\n";
    } else { // Fahrenheit
        if (temp < 32) cout << "solid\n";
        else if (temp < 212) cout << "liquid\n";
        else cout << "gas\n";
    }

    return 0;
}