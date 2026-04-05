#include <iostream>
#include <string>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

string seasons[] = {"winter", "spring", "summer", "fall"};

int main() {
    phuthitj;

    int m, d;
    cin >> m >> d;

    int effective_month = m + (d >= 21 && m % 3 == 0);

    int index = ((effective_month - 1) / 3) % 4;

    cout << seasons[index];

    return 0;
}