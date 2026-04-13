#include <iostream>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

void solve(int n) {
    int ten = 0, five = 0, two = 0, one = 0;

    while (n > 0) {
        if (n >= 10) {
            n -= 10;
            ten++;
        } else if (n >= 5) {
            n -= 5;
            five++;
        } else if (n >= 2) {
            n -= 2;
            two++;
        } else if (n >= 1) {
            n -= 1;
            one++;
        }
    }

    cout << "10 = " << ten << endl;
    cout << "5  = " << five << endl;
    cout << "2  = " << two << endl;
    cout << "1  = " << one << endl;
}

int main() {
    phuthitj;
    int n;
    if (cin >> n) {
        solve(n);
    }
    return 0;
}