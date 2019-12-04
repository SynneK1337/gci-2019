#include <array>
#include <algorithm>
#include <iostream>

int main() {
    // Array creation
    std::array<int, 9> numbers = {4, 5, 2, 9, 10, -5, -10, 8, 21};
    std::array<int, 9> numbers1 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    // Array's items printing
    std::cout << "Unsorted array numbers: ";
    for (const auto &item: numbers) {
        std::cout << item << ", ";
    }

    // Array comparison
    if (numbers == numbers1) {
        std::cout << "Arrays are equal.";
    } else {std::cout << "Arrays are not equal.";}
    return 0;
}