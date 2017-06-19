#include <stdio.h>

int main(){
	int x = 0;
	float r = 0;
	int z = 0;

	for(x = 0; x < 6; x++){
		scanf("%f", &r);
		if(r > 0){
			z++;
		}	
	}

	printf("%d valores positivos\n", z);

	return 0;

}