#include <iostream>
using namespace std;
#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

int main() {
    phuthitj;
    int period, time;
    cin >> period >> time;
    int total_minutes = period * time;
    
    if (total_minutes == 0) {
        cout << "No teaching";
    } else {
        int hours = total_minutes / 60;
        int minutes = total_minutes % 60;

        cout << hours << " hours";

        if (minutes > 0) {
            cout << " " << minutes << " minutes";
        }
    }

    return 0;
}