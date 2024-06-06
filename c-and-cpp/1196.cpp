#include <iostream>
#include <unordered_map>
#include <string>
#include <stdexcept>

std::unordered_map<char, char> qwerty_left_map = {
    {'1', '`'}, {'2', '1'}, {'3', '2'}, {'4', '3'}, {'5', '4'}, {'6', '5'}, {'7', '6'}, {'8', '7'}, {'9', '8'}, {'0', '9'}, 
    {'-', '0'}, {'=', '-'},
    {'Q', '`'}, {'W', 'Q'}, {'E', 'W'}, {'R', 'E'}, {'T', 'R'}, {'Y', 'T'}, {'U', 'Y'}, {'I', 'U'}, {'O', 'I'}, {'P', 'O'}, 
    {'[', 'P'}, {']', '['}, {'\\', ']'},
    {'A', '`'}, {'S', 'A'}, {'D', 'S'}, {'F', 'D'}, {'G', 'F'}, {'H', 'G'}, {'J', 'H'}, {'K', 'J'}, {'L', 'K'}, {';', 'L'}, 
    {'\'', ';'},
    {'Z', '`'}, {'X', 'Z'}, {'C', 'X'}, {'V', 'C'}, {'B', 'V'}, {'N', 'B'}, {'M', 'N'}, {',', 'M'}, {'.', ','}, {'/', '.'},
    {'`', '`'}, {' ', ' '},
    {'!', '`'}, {'@', '!'}, {'#', '@'}, {'$', '#'}, {'%', '$'}, {'^', '%'}, {'&', '^'}, {'*', '&'}, {'(', '*'}, {')', '('},
    {'_', ')'}, {'+', '_'},
    {'{', 'P'}, {'}', '{'}, {'|', '}'}, {':', 'L'}, {'"', ':'}, {'<', 'M'}, {'>', '<'}, {'?', '>'}
};

std::string translateInput(const std::string& input) {
    std::string output;
    for (char c : input) {
        output += qwerty_left_map[c];
    }
    return output;
}

int main() {
    std::string input;
    while (true) {
        if (!std::getline(std::cin, input)) {
            break;
        }
        std::string output = translateInput(input);
        std::cout << output << std::endl;
    }
    return 0;
}
