#include "Thanos.h"
#include <iostream>
#include <vector>

int main() {
	std::vector<float> test_checks{};
	{
		unsigned int number_of_tests;
		std::cout << "[?] How many tests you want to perform? ";
		std::cin >> number_of_tests;
		for (unsigned int i = 0; i < number_of_tests; ++i) {
			float days;
			std::cout << '[' << i + 1 << "] How many days should the battle last? ";
			std::cin >> days;
			test_checks.push_back(days);
		}
	}
	for (const auto& days : test_checks) {
		Thanos t(days);
		std::cout << t.killer << std::endl;
	}
}