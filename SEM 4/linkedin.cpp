#include <iostream>
#include <string>
using namespace std;

void thankYouLoop() {
    string str = "Thank you";
    while (true) {
        str += "Thank you";
        cout << str << endl;
    }
}

int main() {
    try {
        thankYouLoop();
    }
    catch (const std::exception& e) {
        cerr << "Exception caught: " << e.what() << endl;
    }

    return 0;
}
