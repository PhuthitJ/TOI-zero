#include <iostream>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int n1, n2, n3;

int main() {
    phuthitj;
    cin >> n1 >> n2 >> n3;
    if (n1 == n2 && n2 == n3) {
        cout << "all the same";
    } else if (n1 != n2 && n1 != n3 && n2 != n3) {
        cout << "all different";
    } else {
        cout << "neither";
    }

    return 0;
}