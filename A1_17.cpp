#include <iostream>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int y1, m1, d1, y2, m2, d2;
int main() {
    phuthitj;
    cin >> y1 >> m1 >> d1 >> y2 >> m2 >> d2;
    if (y1 == y2 && m1 == m2 && d1 == d2) {
        cout << "0";
    } else if (y1 < y2 || (y1 == y2 && m1 < m2) || (y1 == y2 && m1 == m2 && d1 < d2)) {
        cout << "1";
    } else {
        cout << "2";
    }

    return 0;
}