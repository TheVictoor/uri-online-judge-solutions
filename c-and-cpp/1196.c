#include <stdio.h>
#include <string.h>

#define MAX_INPUT_LENGTH 1024

char qwerty_left_map[128];

void initialize_map() {
    memset(qwerty_left_map, 0, sizeof(qwerty_left_map));
    qwerty_left_map['1'] = '`';
    qwerty_left_map['2'] = '1';
    qwerty_left_map['3'] = '2';
    qwerty_left_map['4'] = '3';
    qwerty_left_map['5'] = '4';
    qwerty_left_map['6'] = '5';
    qwerty_left_map['7'] = '6';
    qwerty_left_map['8'] = '7';
    qwerty_left_map['9'] = '8';
    qwerty_left_map['0'] = '9';
    qwerty_left_map['-'] = '0';
    qwerty_left_map['='] = '-';
    qwerty_left_map['Q'] = '`';
    qwerty_left_map['W'] = 'Q';
    qwerty_left_map['E'] = 'W';
    qwerty_left_map['R'] = 'E';
    qwerty_left_map['T'] = 'R';
    qwerty_left_map['Y'] = 'T';
    qwerty_left_map['U'] = 'Y';
    qwerty_left_map['I'] = 'U';
    qwerty_left_map['O'] = 'I';
    qwerty_left_map['P'] = 'O';
    qwerty_left_map['['] = 'P';
    qwerty_left_map[']'] = '[';
    qwerty_left_map['\\'] = ']';
    qwerty_left_map['A'] = '`';
    qwerty_left_map['S'] = 'A';
    qwerty_left_map['D'] = 'S';
    qwerty_left_map['F'] = 'D';
    qwerty_left_map['G'] = 'F';
    qwerty_left_map['H'] = 'G';
    qwerty_left_map['J'] = 'H';
    qwerty_left_map['K'] = 'J';
    qwerty_left_map['L'] = 'K';
    qwerty_left_map[';'] = 'L';
    qwerty_left_map['\''] = ';';
    qwerty_left_map['Z'] = '`';
    qwerty_left_map['X'] = 'Z';
    qwerty_left_map['C'] = 'X';
    qwerty_left_map['V'] = 'C';
    qwerty_left_map['B'] = 'V';
    qwerty_left_map['N'] = 'B';
    qwerty_left_map['M'] = 'N';
    qwerty_left_map[','] = 'M';
    qwerty_left_map['.'] = ',';
    qwerty_left_map['/'] = '.';
    qwerty_left_map['`'] = '`';
    qwerty_left_map[' '] = ' ';
    qwerty_left_map['!'] = '`';
    qwerty_left_map['@'] = '!';
    qwerty_left_map['#'] = '@';
    qwerty_left_map['$'] = '#';
    qwerty_left_map['%'] = '$';
    qwerty_left_map['^'] = '%';
    qwerty_left_map['&'] = '^';
    qwerty_left_map['*'] = '&';
    qwerty_left_map['('] = '*';
    qwerty_left_map[')'] = '(';
    qwerty_left_map['_'] = ')';
    qwerty_left_map['+'] = '_';
    qwerty_left_map['{'] = 'P';
    qwerty_left_map['}'] = '{';
    qwerty_left_map['|'] = '}';
    qwerty_left_map[':'] = 'L';
    qwerty_left_map['"'] = ':';
    qwerty_left_map['<'] = 'M';
    qwerty_left_map['>'] = '<';
    qwerty_left_map['?'] = '>';
}

void translateInput(const char* input, char* output) {
    while (*input) {
        char c = *input;
        *output = qwerty_left_map[(int)c];
        input++;
        output++;
    }
    *output = '\0';
}

int main() {
    initialize_map();

    char input[MAX_INPUT_LENGTH];
    char output[MAX_INPUT_LENGTH];

    while (1) {
        if (!fgets(input, sizeof(input), stdin)) {
            break;
        }

        input[strcspn(input, "\n")] = '\0';

        translateInput(input, output);
        printf("%s\n", output);
    }

    return 0;
}
