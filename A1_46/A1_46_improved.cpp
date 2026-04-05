#include <iostream>
using namespace std;
#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int main() {
    phuthitj;
    int n; cin >> n;

    long long total_sum = 0;
    int even_count = 0;
    int odd_count = 0;
    int num;

    for (int i = 0; i < n; i++) {
        cin >> num;
        total_sum += num;
        if (num % 2 == 0) {
            even_count++;
        } else {
            odd_count++;
        }
    }

    cout << "SUM " << total_sum << "\n";
    cout << "EVEN " << even_count << "\n";
    cout << "ODD " << odd_count << "\n";

    return 0;
}