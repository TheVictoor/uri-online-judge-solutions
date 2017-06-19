#include <stdio.h>

int main(){
	int v, x;
	v = x = 0;

	scanf("%d", &v);

	for(x = 1; x <= v; x++){
		if(x % 2 == 1){
			printf("%d\n", x);
		}
	}
	return 0;	
}