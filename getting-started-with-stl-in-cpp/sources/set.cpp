#include <set>
#include <iostream>

int main() {
    // std::set creation
    std::set<int> set;

    // insert a value into std::set
    set.insert(420);
    set.insert(10);
    set.insert(20);
    set.insert(10);
    set.insert(30);

    // Printing the values of std::set
    std::cout << "Unmodified set: " << std::endl;
    for (const auto &value : set) {
        std::cout << value << std::endl;
    }
    // Delete values lower than 20 from std::set
    set.erase(set.begin(), set.find(20));

    std::cout << "set after deleting values lower than 20" << std::endl;
    for (const auto &value: set) {
        std::cout << value << std::endl;
    }
    return 0;
}