#include <stdio.h>

int main(){
	int c, v, x;
	c = v = x = 0;

	for(x = 0; x < 5; x++){
		scanf("%d", &v);
		if(v % 2 == 0){
			c++;
		}
	}

	printf("%d valores pares\n", c);
	return 0;
}