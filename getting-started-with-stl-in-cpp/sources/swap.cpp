#include <algorithm>
#include <iostream>
 
int main() {
    // Creating the int values
    int a = 14;
    int b = 21;

    // Printing them
    std::cout << "a = " << a << ", b = " << b << std::endl;

    // Swapping them
    std::swap(a, b);

    // Printing values after swap
    std::cout << "a = " << a << ", b = " << b << std::endl;
}
