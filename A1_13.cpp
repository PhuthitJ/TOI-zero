#include <iostream>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

char key;
int pwd;
int main() {
    phuthitj;
    cin >> key >> pwd;
    if (key == 'H' && pwd == 4567) {
        cout << "safe unlocked";
    } else if (key == 'h' && pwd == 4567) {
        cout << "safe locked - change char";
    } else if (key == 'H' && pwd != 4567) {
        cout << "safe locked - change digit";
    } else {
        cout << "safe locked";
    }

    return 0;
}