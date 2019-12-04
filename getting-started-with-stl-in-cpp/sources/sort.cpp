#include <algorithm>
#include <array>
#include <vector>
#include <iostream>

int main() {
    // std::vector and std::array creation
    std::array<int, 9> array = {4, 2, 1, 9, -10, -20, 8, 19, 60};
    std::vector<int> vector = {8, 2, 10, -50};

    // Printing std::array and std::vector
    std::cout << "Unsorted array values: ";
    for (const auto &value: array) {
        std::cout << value << ", ";
    }
    std::cout << std::endl << "Unsorted vector values: ";
    for (const auto &value: vector) {
        std::cout << value << ", ";
    }

    // std::vector and std::array sorting
    std::sort(array.begin(), array.end());
    std::sort(vector.begin(), vector.end());

    // Printing sorted std::array and std::vector
    std::cout << std::endl << "Sorted array values: ";
    for (const auto &value: array) {
        std::cout << value << ", ";
    }
    std::cout << std::endl << "Sorted vector values: ";
    for (const auto &value: vector) {
        std::cout << value << ", ";
    }
}