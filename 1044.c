#include <stdio.h>

int main(){
	int x, m, i;
	x = m = 0;

	scanf("%d %d", &x , &m);

	if(x % m == 0 || m % x == 0){
		printf("Sao Multiplos\n");
	}else {
		printf("Nao sao Multiplos\n");
	}
	
	return 0;

}