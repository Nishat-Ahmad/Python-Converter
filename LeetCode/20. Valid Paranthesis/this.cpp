#include <iostream>
#include <stack>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> thisStack;

        for (char ch : s) {
            if (ch == '(' || ch == '{' || ch == '[') {
                thisStack.push(ch);
            } else {
                if (thisStack.empty()) return false;  // No matching opening bracket
                char top = thisStack.top();
                if ((ch == ')' && top == '(') || 
                    (ch == '}' && top == '{') || 
                    (ch == ']' && top == '[')) {
                    thisStack.pop();
                } else {
                    return false;  // Mismatched bracket
                }
            }
        }
        
        return thisStack.empty();  // Check if all opening brackets have been matched
    }
};

int main(){
    cout << isValid("]");
}