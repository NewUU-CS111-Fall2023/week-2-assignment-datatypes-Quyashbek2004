#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
std::string generateRandomNumber(int numDigits) {
    std::string randomNumber = "";

    for (int i = 0; i < numDigits; i++) {
        int digit = rand() % 10;
        randomNumber += std::to_string(digit);
    }

    return randomNumber;
}

int main() {
    int A;
    std::cout << "Enter a number (A): ";
    std::cin >> A;

    srand(static_cast<unsigned int>(time(0)));
    std::string number = generateRandomNumber(100);

    // Perform the division
    std::string result = "";
    int carry = 0;
    for (int i = 0; i < 100; i++) {
        int digit = carry * 10 + (number[i] - '0');
        result += std::to_string(digit / A);
        carry = digit % A;
    }

    std::cout << "Result of dividing the 100-digit number by " << A << ":" << std::endl;
    std::cout << result << std::endl;

    return 0;
}

