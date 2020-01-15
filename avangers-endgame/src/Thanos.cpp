#include "Thanos.h"
#include <cmath>

Thanos::Thanos(float hp) {
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
