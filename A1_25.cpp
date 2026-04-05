#include <iostream>
#include <string>

#define phuthitj ios_base::sync_with_stdio(false); cin.tie(NULL);

using namespace std;

int main() {
    phuthitj;
    string input;
    cin >> input;

    char suitChar = input[input.length() - 1];
    
    string rankStr = input.substr(0, input.length() - 1);

    string rankName;
    string suitName;

    if (rankStr == "A" || rankStr == "a") rankName = "ace";
    else if (rankStr == "J" || rankStr == "j") rankName = "jack";
    else if (rankStr == "Q" || rankStr == "q") rankName = "queen";
    else if (rankStr == "K" || rankStr == "k") rankName = "king";
    else {
        rankName = rankStr;
    }

    if (suitChar == 'D' || suitChar == 'd') suitName = "diamonds";
    else if (suitChar == 'H' || suitChar == 'h') suitName = "hearts";
    else if (suitChar == 'S' || suitChar == 's') suitName = "spades";
    else if (suitChar == 'C' || suitChar == 'c') suitName = "clubs";

    cout << rankName << " of " << suitName << endl;

    return 0;
}