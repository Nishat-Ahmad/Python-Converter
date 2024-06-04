#include <iostream>
#include <string>

using namespace std;

bool isPalindrome(int x) {
        string str;
        str = to_string(x);

        if (str[0] == '-'){
                return false;
        }

        size_t len = str.size();
        

        for(size_t i = 0; i < len / 2; i++){

            cout << (str[len - i]) << endl;
            if(&(str[i]) == &(str[len - i])){
                break;
            }
            if(&(str[i]) == &(str[len - i])){
                //  val = true;
            } if(&(str[i]) != &(str[len - i])){
                break;
            }
        }
        return true;
}

bool isPalindrome(int x) {
    if (x < 0)
        return false;

    string str = to_string(x);
    size_t len = str.size();

    for (size_t i = 0; i < len / 2; ++i) {
        if (str[i] != str[len - i - 1]) {
            return false;
        }
    }
    return true;
}

int main(){
    cout << isPalindrome(-121);
}