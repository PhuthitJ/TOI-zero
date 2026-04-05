#include <iostream>
#include <vector>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

vector<int> PP;
vector<int> EO;

int main() {
    phuthitj;
    long long p;
    cin >> p;
    if (p < 1) {
        p = 500000;
    }

    for (int i = 0; i < p * p; i++) {
        int n;
        cin >> n;
        PP.push_back(n);
    }

    if (sizeof(PP) != p * p) {
        return 0;
    }

    for (int i = 0; i < sizeof(PP); i++) {
        if (PP[i] % 2 == 0) {
            EO[i] = 0;
        } else {
            EO[i] = 1;
        }
    }

    int player_odd, player_even = p;
    int cnt = 0;

    for (int i = 0; i < sizeof(EO); i++) {
        if (EO[i] == 0) {
            player_odd--;
        } else {
            player_even--;
        }
    }

    cout << player_odd << " " << player_even << endl;

    return 0;
}