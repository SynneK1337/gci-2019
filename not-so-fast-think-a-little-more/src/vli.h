#pragma once
#include <vector>
class vli {
public:
	std::vector<unsigned short> digits;
	size_t count;
	vli(std::vector<unsigned short> digits);
	void print();
	void add(std::vector<unsigned short> b);
	void multiply(std::vector<unsigned short> b);
	void pow(unsigned long long b);
};

std::vector<unsigned short> number_to_vector(unsigned long long number);