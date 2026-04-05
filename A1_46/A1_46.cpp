#include <iostream>
#include <vector>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int main() {
    phuthitj;
    vector<int> arr;
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        arr.push_back(num);
    }
    int sum = 0;
    for (int i : arr) {
        sum += i;
    }
    int even_sum = 0;
    for (int i : arr) {
        if (i % 2 == 0) {
            even_sum += 1;
        }
    }
    int odd_sum = 0;
    for (int i : arr) {
        if (i % 2 != 0) {
            odd_sum += 1;
        }
    }

    cout << "SUM " << sum << "\n";
    cout << "EVEN " << even_sum << "\n";
    cout << "ODD " << odd_sum << "\n";

    return 0;
}