# Getting started with STL in C++
### This article was made for Google Code-In 2019 challange 
## What is STL?
**STL** stands for **Standard Template Library** and it is a part of **C++ Standard Library**.

## What does STL provide?
- Containers *(such as ```std::vector``` or ```std::array```)*
- Iterators *(defined in ```<iterator>```)*
- Algortims *(e.g ```std::sort()```)*
- Functions *(for example ```std::transform()```)*

## Containers
There are few containers available within **STL**:
### **std::vector**
In other words, ```std::vector``` is just dynamic array. It' s size may get changed during the runtime.
#### ```std::vector``` usage:
```c++
#include <vector>
#include <iostream>
int main() {
    // Create a vector of ints called numbers
    std::vector<int> numbers;

    // Add items to the end of numbers
    numbers.push_back(2);
    numbers.push_back(3);

    // Add item at the begin of numbers
    numbers.insert(numbers.begin(), 1);

    // Print elements of numbers
    for (const auto &item : numbers){
        std::cout << item << std::endl; 
    }
    return 0;
}
```
And after compilation and execution we got following output:
```
1
2
3
```
For more informations about ```std::vector``` I suggest checking out [cppreference](https://en.cppreference.com/w/cpp/container/vector)
### **std::array**
```std::array``` is just a bit improved implementation of **C-Style arrays** known from **C**.
#### Benefits of ```std::array``` over ```C-style array```:
- Iterators such as:
    - ```.begin()``` which points to the begin of an array
    - ```.end()``` which points to the end of an array
    - ```.rbegin()``` which points to the end of an array
    - ```.rend()``` which points to the begin of an array

- Compatibility with algoritms such as:
    - ```std::sort()``` which sorts array ascending
    - ```std::swap()``` which swaps values

- Overloaded operators ```==, !=, <, >, >=, <=``` which allows us to easily compare two arrays

#### ```std::array``` usage:
```c++
#include <array>
#include <iostream>

int main() {
    // Array creation
    std::array<int, 9> numbers = {4, 5, 2, 9, 10, -5, -10, 8, 21};
    std::array<int, 9> numbers1 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    // Array's items printing
    std::cout << "Unsorted array numbers: ";
    for (const auto &item: numbers) {
        std::cout << item << ", ";
    }
    // Array comparison
    if (numbers == numbers1) {
        std::cout << "Arrays are equal.";
    } else {std::cout << "Arrays are not equal.";}
    return 0;
}
```
After compilation and execution we got following results:
```
Unsorted array numbers: 4, 5, 2, 9, 10, -5, -10, 8, 21, 
Sorted array numbers: -10, -5, 2, 4, 5, 8, 9, 10, 21,
Arrays are not equal.
```
For more information about ```std::array``` I suggest checking out [cppreference](https://en.cppreference.com/w/cpp/container/array).

### **std::set**
```std::set``` is the type of container that stores **unique** values which can' t be modified, though you can remove and then add modified value.

#### ```std::set``` usage:
```c++
#include <set>
#include <iostream>

int main() {
    // std::set creation
    std::set<int> set;

    // insert a value into std::set
    set.insert(420);
    set.insert(10);
    set.insert(20);
    set.insert(10); // 10 value will not be inserted since set stores only unique values
    set.insert(30);

    // Printing the values of std::set
    std::cout << "Unmodified set: " << std::endl;
    for (const auto &value : set) {
        std::cout << value << std::endl;
    }
    // Delete values lower than 20 from std::set
    set.erase(set.begin(), set.find(20));

    std::cout << "set after deleting values lower than 20" << std::endl;
    for (const auto &value: set) {
        std::cout << value << std::endl;
    }
    return 0;
}
```
After compilation and execution of this code we got following output:
```
Unmodified set: 
10
20
30
420
set after deleting values up to 20
20
30
420
```
For more informations about ```std::set``` I suggest checking out [cppreference](https://en.cppreference.com/w/cpp/container/set)

### **std::map**
If you are familiar with ```python``` language, you could probably heard of ```dictionary``` variable type. ```std::map``` is very similiar to python' s dictionaries.
Long story short: ```std::map``` is vector of ```std::pair``` that stores **key** and it's **value**.

#### ```std::map``` usage:
```c++
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
```
After compilation and execution of this code we got following output:
```
Emilian: 15
Paul: 14

students_ages keys:
Emilian
John
Paul

students_ages values:
15
21
14

students_ages pairs:
Emilian -> 15
John -> 21
Paul -> 14
```
For more informations about ```std::map``` I suggest checking out [cppreference](https://en.cppreference.com/w/cpp/container/map).

## Algorithms
STL' s algorithms are pretty useful while working with containers. I will show you usage for some of them below.

### **std::sort()** usage:
```c++
#include <algorithm>
#include <array>
#include <vector>
#include <iostream>

int main() {
    // std::vector and std::array creation
    std::array<int, 9> array = {4, 2, 1, 9, -10, -20, 8, 19, 60};
    std::vector<int> vector = {8, 2, 10, -50};

    // Printing std::array and std::vector
    std::cout << "Unsorted array values: ";
    for (const auto &value: array) {
        std::cout << value << ", ";
    }
    std::cout << std::endl << "Unsorted vector values: ";
    for (const auto &value: vector) {
        std::cout << value << ", ";
    }

    // std::vector and std::array sorting
    std::sort(array.begin(), array.end());
    std::sort(vector.begin(), vector.end());

    // Printing sorted std::array and std::vector
    std::cout << std::endl << "Sorted array values: ";
    for (const auto &value: array) {
        std::cout << value << ", ";
    }
    std::cout << std::endl << "Sorted vector values: ";
    for (const auto &value: vector) {
        std::cout << value << ", ";
    }
}
```
After compiling and execution this code we got following results:
```
Unsorted array values: 4, 2, 1, 9, -10, -20, 8, 19, 60, 
Unsorted vector values: 8, 2, 10, -50,
Sorted array values: -20, -10, 1, 2, 4, 8, 9, 19, 60,
Sorted vector values: -50, 2, 8, 10,
```
For more informations about ```std::sort()``` I suggest checking out [cppreference](https://en.cppreference.com/w/cpp/algorithm/sort)

### **std::swap()** usage:
```c++
#include <algorithm>
#include <iostream>
 
int main() {
    // Creating the int values
    int a = 14;
    int b = 21;

    // Printing them
    std::cout << "a = " << a << ", b = " << b << std::endl;

    // Swapping them
    std::swap(a, b);

    // Printing values after swap
    std::cout << "a = " << a << ", b = " << b << std::endl;
}
```
After compilation and executing this code we got following results:
```
a = 14, b = 21
a = 21, b = 14
```
For more informations about ```std::swap()``` I suggest checking out [cppreference](https://en.cppreference.com/w/cpp/algorithm/swap)
## **std::string**
Similary to ```std::array```, ```std::string``` is an improved implementation of ```C-style string```. \
Advantages of ```std::string``` over ```C-style string```:
- Non-constant length
- Overloaded operators such as ```=``` or ```==``` so you don' t need to use ```strcpy()``` or ```strcmp()``` anymore.

### ```std::string``` usage:
```c++
#include <string>
#include <iostream>

int main() {
    // std::string creation
    std::string name = "Emilian";

    // Printing std::string
    std::cout << name << std::endl;

    // Adding last name into name
    name += " Zawrotny";

    // Printing std::string after modification
    std::cout << name << std::endl;

    // Getting length of std::string
    std::cout << "Length of name: " << name.length() << std::endl;

    // Comparing two strings
    std::string newString = "Emilian Zawrotny";
    if (newString == name) {
        std::cout << "Strings are equal." << std::endl;
    } else {
        std::cout << "Strings are not equal." << std::endl;
    }

    std::string thirdString = "abcdef";
    if (thirdString == name) {
        std::cout << "Strings are equal." << std::endl;
    } else {
        std::cout << "Strings are not equal." << std::endl;
    }
    return 0;
}
```
After compilation and execution of this code, we got following output:
```
Emilian
Emilian Zawrotny
Length of name: 16
Strings are equal.
Strings are not equal.
```
## Made with **<3** by Emilian `synnek1337` Zawrotny
### 2019 © All rights reserved