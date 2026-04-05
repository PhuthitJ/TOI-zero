#include <iostream>
#include <string>
using namespace std;

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int main() {
    phuthitj;
    
    string s;
    cin >> s;
    
    int count = 1;
    
    for (int i = 0; i < s.length(); i++) {
        
        if (i + 1 < s.length() && s[i] == s[i+1]) {
            count++;
        } 
        else {
            cout << count << s[i]; 
            count = 1;
        }
    }
    
    return 0;
}