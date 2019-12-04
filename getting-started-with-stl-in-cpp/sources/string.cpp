#include <string>
#include <iostream>

int main() {
    // std::string creation
    std::string name = "Emilian";

    // Printing std::string
    std::cout << name << std::endl;

    // Adding last name into name
    name += " Zawrotny";

    // Printing std::string after modification
    std::cout << name << std::endl;

    // Getting length of std::string
    std::cout << "Length of name: " << name.length() << std::endl;

    // Comparing two strings
    std::string newString = "Emilian Zawrotny";
    if (newString == name) {
        std::cout << "Strings are equal." << std::endl;
    } else {
        std::cout << "Strings are not equal." << std::endl;
    }

    std::string thirdString = "abcdef";
    if (thirdString == name) {
        std::cout << "Strings are equal." << std::endl;
    } else {
        std::cout << "Strings are not equal." << std::endl;
    }
    return 0;
}