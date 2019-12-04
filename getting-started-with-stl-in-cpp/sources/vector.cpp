#include <vector>
#include <iostream>
int main() {
    // Create a vector of ints called numbers
    std::vector<int> numbers;

    // Add items to the end of numbers
    numbers.push_back(2);
    numbers.push_back(3);

    // Add item at the begin of numbers
    numbers.insert(numbers.begin(), 1);

    // Print elements of numbers
    for (const auto &item : numbers){
        std::cout << item << std::endl; 
    }
    return 0;
}