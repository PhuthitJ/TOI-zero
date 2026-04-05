#include <iostream>
#include <iomanip>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int main() {
    phuthitj;
    int unit;
    double price;
    bool temp = true;
    cin >> unit;
    
    double FT = 0.5 * unit;
    
    while (temp) {
        if (unit == 1) {
            price += 5;
            temp = false;
        } else if (unit > 1 && unit <= 10) {
            price += 5;
            unit -= 1;
        } else if (unit >= 11 && unit <= 50) {
            price += 7;
            unit -= 1;
        } else if (unit >= 51 && unit <= 100) {
            price += 10;
            unit -= 1;
        } else if (unit >= 101 && unit <= 200) {
            price += 12;
            unit -= 1;
        } else {
            price += 15;
            unit -= 1;
        }
    }

    double VAT = price * 0.07;
    
    price = price + VAT + FT;
    
    cout << fixed << setprecision(2);
    cout << price << endl;
    
    return 0;
}