#include <iostream>
#include <random>
#include <chrono>
#include <array>

constexpr short TABLE_WIDTH     = 20;
constexpr short TABLE_HEIGHT    = 20;
constexpr short QUEENS          = 20;

class Queen {
    private:
        bool check_availability(const short x, const short y, std::array<std::array<bool, TABLE_HEIGHT>, TABLE_WIDTH> &table) {
            // Check horizontally
            for (const bool &v: table[x]) {
                if (v == true) {
                    return false;
                }
            }
            // Check vertically
            for (const auto &v: table) {
                if (v[y] == true) {
                    return false;
                }
            }
            // Returns true if available
            return true;
        }
        
    public:
        bool placed = false;
        Queen(const short x, const short y, std::array<std::array<bool, TABLE_HEIGHT>, TABLE_WIDTH> &table) {
            if (check_availability(x, y, table) == true) {
                table[x][y] = true;
                this->placed = true;
            }
        }
};

int randint(int min, int max, std::mt19937 &engine) {
    std::uniform_int_distribution<int> gen(min, max);
    return gen(engine);
}

void fill_table_with_falses(std::array<std::array<bool, TABLE_HEIGHT>, TABLE_WIDTH> &table) {
    for (auto &x: table) {
        for (auto &y: x) {
            y = false;
        }
    }
}

void print_table(std::array<std::array<bool, TABLE_HEIGHT>, TABLE_WIDTH> &table) {
    for (const auto &x: table) {
        for (short i=1; i<=TABLE_WIDTH; ++i) {
            std::cout << "+---";
        }
        std::cout << '+' << std::endl;
        for (const auto &y: x) {
            if (y == true) {
                std::cout << "| * ";
            } else {
                std::cout << "|   ";
            }
        }
        std::cout << '|' << std::endl;
    }
    for (short i=1; i<=TABLE_WIDTH; ++i) {
        std::cout << "+---";
    }
    std::cout << '+';
}

int main() {
    const unsigned seed = static_cast<unsigned>(std::chrono::high_resolution_clock().now().time_since_epoch().count());
    std::mt19937 engine(seed);
    // Table initialization
    std::array<std::array<bool, TABLE_HEIGHT>, TABLE_WIDTH> table;
    fill_table_with_falses(table);

    // Putting queens on table
    short placed_queens = 0;
    while (placed_queens < QUEENS) {
        const int x = randint(0, TABLE_WIDTH-1, engine);
        const int y = randint(0, TABLE_HEIGHT-1, engine);
        Queen *queen = new Queen(x, y, table);

        // Queen() constructor checks if both row and column is available
        // If they are available, it puts true to this random point in array
        // and change value of placed to true
        if (queen->placed == true) {
            ++placed_queens;
            std::cout << "[i] Placed queens: " << x << ", " << y << std::endl;
        }
        // Free queen from memory to avoid memory leak
        delete queen;
    }
    // Printing complete solution to the screen
    print_table(table);
}
