#include <stdio.h>

int main(){
	int v, x, c;
	v = x = c = 0;

	scanf("%d", &v);
	v += v % 2 == 0 ? 1 : 0;

	for(x = 0; x < 6; x++){
		printf("%d\n", v);
		v += 2;
	}

	return 0;
	
}