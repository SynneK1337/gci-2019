from dataclasses import dataclass

@dataclass
class Element():
    atomic_number:  int
    name:           str
    period:         int
    group:          int
    symbol:         str
