#include <iostream>

using namespace std;

int romanToInt(string s) {
    int total = 0;
    int prevValue = 0;
    
    for (char current : s) {
        int currValue = value(current);
        
        if (currValue > prevValue) {
            total += currValue - 2 * prevValue; // Subtract the previously added smaller value
        } else {
            total += currValue;
        }
        
        prevValue = currValue;
    }
    
    return total;
}

int value(char r) {
    switch (r) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return 0;
    }
}

int main(){
    cout << romanToInt("XXVII");
}