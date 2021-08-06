#include <stdio.h>

int main(){
	int x[20];
	int i = 19;
	int y , a;

	for(y = 0; y < 20; y++ ){
		scanf("%i", &x[y]);
	}


	for(y = 0, i = 19; y < 10; y++, i--){
		a = x[i];
		x[i] = x[y];
		x[y] = a;
	}

	for(y = 0; y < 20; y++){
		printf("N[%d] = %d\n", y , x[y]);
	}

	return 0;
}