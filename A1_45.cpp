#include <iostream>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int main() {
    phuthitj;
    int distance;
    int price = 0;
    bool temp = true;
    cin >> distance;
    while (temp) {
        if (distance == 1) {
            price += 35;
            distance -= 1;
            temp = false;
        } else if (distance > 1 && distance <= 10) {
            price += 5;
            distance -= 1;
        } else {
            price += 8;
            distance -= 1;
        }
    }

    cout << price << endl;

    return 0;
}