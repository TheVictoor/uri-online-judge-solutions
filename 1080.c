#include <stdio.h>

int main(){
	int v, x, pos, maior;

	v = x = pos = maior = 0;

	for(x = 1; x <= 100; x++ ){
		scanf("%d", &v);
		if(v > maior){
			maior = v;
			pos = x;
		}
	}	

	printf("%d\n%d\n", maior, pos );

	return 0;
}