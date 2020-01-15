#pragma once
#include <string>
class Thanos {
public:
	float hp;
	Thanos(float hp);
	unsigned long long days_needed_to_kill = 0;
	std::string killer;
};

