#include <iostream>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int main() {
    int midterm, finalterm, total;
    phuthitj;
    cin >> midterm >> finalterm;
    total = midterm + finalterm;

    if (total > 50) {
        cout << total << endl << "pass";
    } else {
        cout << total << endl << "fail";
    }

    return 0;
}