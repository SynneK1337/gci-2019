#include "vli.h"
#include <iostream>

int main() {
	vli* v1 = new vli(number_to_vector(2));
	unsigned long long n;
	while (1) {
		std::cout << "[?] Enter number between 0-1024: ";
		std::cin >> n;
		if (0 <= n && n <= 1024) {
			break;
		}
	}
	
	v1->pow(n);
	v1->print();

	delete v1;
}