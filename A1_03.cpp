#include <iostream>
#include <algorithm>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int main() {
    phuthitj;
    
    int a, b, c;
    
    cin >> a >> b >> c;
    
    cout << max({a, b, c});
    
    return 0;
}