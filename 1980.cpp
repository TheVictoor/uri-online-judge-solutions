#include <iostream>
using namespace std;

uint64_t fat (int n) {
	uint64_t f = 1;
	for (int i = n; i >= 1; i--) {
		f *= i;
	}
	return f;
}

int main(int argc, char *argv[]) {
	string palavra;
	while (1) {
		cin >> palavra;

		if (palavra == "0") 
			break;

		cout << fat(palavra.size()) << endl;
	}
	
	return 0;
}