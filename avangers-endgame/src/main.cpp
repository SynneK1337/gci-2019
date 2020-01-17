#include <string>
#include <iostream>
#include <vector>
#include <cmath>

class Thanos {
public:
	float hp;
	std::string killer;
	unsigned long long days_needed_to_kill = 0;
	Thanos(float hp) {
		this->hp = hp;
		if (this->hp > 1) {
			// hp - 1 because they deal for D+1 on the last day
			// Modern Problems Requires Modern Solutions
			this->days_needed_to_kill = std::ceil(-0.5 + std::sqrt((0.25 + 2 * (this->hp - 1))));
		}
		else {
			this->days_needed_to_kill = std::ceil(-0.5 + std::sqrt((0.25 + 2 * this->hp)));
		}
		
		this->killer = (days_needed_to_kill % 2 == 0) ? "Captain America" : "Iron man";
	}
};



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