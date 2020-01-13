#include "vli.h"
#include <iostream>
#include <cmath>
#include <algorithm>

vli::vli(std::vector<unsigned short> digits) {
	this->digits = digits;
	this->count = this->digits.size();
}

void vli::add(std::vector<unsigned short> b) {
	if (b.size() > this->count) {
		std::swap(b, this->digits);
		this->count = this->digits.size();
	}
	size_t b_count = b.size();
	// Maximum length of result of sum is (length of longest element + 1)
	this->digits.push_back(0);
	++this->count;

	for (size_t i = 0; i < this->count - 1; ++i) {
		if (i < b_count) {
			this->digits[i] += b[i];
			this->digits[i + 1] += this->digits[i] / 10;
			this->digits[i] %= 10;
		}
	}
	if (this->digits[this->count - 1] == 0) {
		this->digits.erase(std::end(this->digits) - 1);
		--this->count;
	}
}

void vli::print() {
	std::reverse(this->digits.begin(), this->digits.end());
	for (const auto& d : digits) {
		std::cout << d;
	}
	std::cout << std::endl;
	std::reverse(this->digits.begin(), this->digits.end());
}

void vli::multiply(std::vector<unsigned short> b) {
	size_t b_count = b.size();
	if (b_count > this->count) {
		std::swap(this->digits, b);
		std::swap(this->count, b_count);
	}
	vli* results = new vli(number_to_vector(0));

	if (b == number_to_vector(10)) {
		this->digits.insert(std::begin(this->digits), 0);
	}
	else {
		for (size_t m = 0; m < b_count; ++m) {
			vli* tmp = new vli(this->digits);
			tmp->count += 1;
			tmp->digits.push_back(0);

			for (auto& a : tmp->digits) {
				a *= b[m];
			}

			for (size_t digit = 0; digit < tmp->count - 1; ++digit) {
				tmp->digits[digit + 1] += tmp->digits[digit] / 10;
				tmp->digits[digit] %= 10;
			}

			if (tmp->digits[tmp->count - 1] == 0) {
				tmp->digits.pop_back();
			}
			for (size_t z = 0; z < m; ++z) {
				auto begin = tmp->digits.begin();
				begin = tmp->digits.insert(begin, 0);
			}
			results->add(tmp->digits);
			delete tmp;
		}
		std::swap(*this, *results);
	}
}

void vli::pow(unsigned long long b) {
	if (b == 0) {
		this->digits = number_to_vector(1);
		this->count = 1;
	}
	std::vector<unsigned short> original_digits = this->digits;
	for (size_t i = 0; i < b - 1; ++i) {
		this->multiply(original_digits);
	}
}

std::vector<unsigned short> number_to_vector(unsigned long long number) {
	if (number < 10) {
		return { static_cast<unsigned short>(number) };
	}
	else if (number == 10) {
		return { 0, 1 };
	}
	else {
		size_t count = std::ceil(std::log10(number));
		std::vector<unsigned short> digits{ 0 };

		for (size_t i = count; i > 0; --i) {
			unsigned short d = std::floor(number / std::pow(10, i - 1));
			for (size_t p = 0; p < digits.size(); ++p) {
				d -= (digits[p] * std::pow(10, (p + 1)));
			}
			auto begin = digits.begin();
			begin = digits.insert(begin, d);
		}
		digits.pop_back();
		return digits;
	}
	
}