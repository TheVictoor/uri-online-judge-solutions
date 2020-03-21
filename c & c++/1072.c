#include <stdio.h>

int main(){
	int x, v, ci, co, z;
	x = v =  ci = co = z =0;

	scanf("%d", &v);

	for(x = 0; x < v; x++){
		scanf("%d", &z);
		if(z >= 10 && z <= 20){
			ci++;
		}else {
			co++;
		}
	}

	printf("%d in\n", ci);
	printf("%d out\n", co );

	return 0;
}