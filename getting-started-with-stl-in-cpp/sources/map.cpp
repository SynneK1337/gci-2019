#include <map>
#include <string>
#include <iostream>

int main() {
    // std::map creation
    std::map<std::string, int> students_ages;
    
    // Inserting values into std::map
    students_ages.insert(std::pair<std::string, int>("John", 21));
    students_ages.insert(std::pair<std::string, int>("Emilian", 15));
    students_ages.insert(std::pair<std::string, int>("Paul", 14));

    // Getting value of the key
    std::cout << "Emilian: " << students_ages["Emilian"] << std::endl;
    std::cout << "Paul: " << students_ages["Paul"] << std::endl;

    // Getting keys from std::map
    std::cout << "\nstudents_ages keys: " << std::endl;
    for (const auto &value: students_ages) {
        std::cout << value.first << std::endl;
    }

    // Getting values from std::map
    std::cout << "\nstudents_ages values: " << std::endl;
    for (const auto &value: students_ages) {
        std::cout << value.second << std::endl;
    }

    // Getting pairs from std::map
    std::cout << "\nstudents_ages pairs: " << std::endl;
    for (const auto &value: students_ages) {
        std::cout << value.first << " -> " << value.second << std::endl;
    }

    return 0;
}