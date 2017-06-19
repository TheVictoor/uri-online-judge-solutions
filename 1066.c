#include <stdio.h>

int main(){
	int par, impar, pos, neg;
	par = impar = pos = neg = 0;

	int v , x;
	x = v = 0;

	for(x = 0; x < 5; x++){
		scanf("%d", &v);
		if(v % 2 == 0){
			par++;
		}else{
			impar++;
		}
		if(v > 0){
			pos++;
		}else if(v < 0){
			neg++;
		}
	}

	printf("%d valor(es) par(es)\n", par);
	printf("%d valor(es) impar(es)\n", impar);
	printf("%d valor(es) positivo(s)\n", pos);
	printf("%d valor(es) negativo(s)\n", neg);

	return 0;

}