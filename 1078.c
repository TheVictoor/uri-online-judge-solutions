#include <stdio.h>

int main(){
	int n, x;
	n = x = 0;

	scanf("%d", &n);

	for(x = 1; x <= 10; x++){
		printf("%d x %d = %d\n", x, n, x * n);
	}

	return 0;
}