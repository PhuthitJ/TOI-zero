#include <iostream>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

char vowels[] = {'a', 'e', 'i', 'o', 'u'};

int main() {
    phuthitj;

    char ch;
    cin >> ch;

    for (char v : vowels) {
        if (ch == v) {
            cout << "yes";
            return 0;
        }
    }
    cout << "no";

    return 0;
}