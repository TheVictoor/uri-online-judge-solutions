#include <stdio.h>

int main(){
	int x, n;
	x = n = 0;

	scanf("%d", &n);

	for(x = 1; x <= 10000; x++){
		if(x % n == 2){
			printf("%d\n", x);
		}
	}	
	return 0;
}