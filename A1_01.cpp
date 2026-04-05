#include <iostream>
#include <string>
using namespace std;

int main() {
    string fn;
    cin >> fn;
    string ln;
    cin >> ln;
    cout << "Hello " << fn << " " << ln << endl;
    cout << fn.substr(0,2) << ln.substr(0,2);
    
    return 0;
}