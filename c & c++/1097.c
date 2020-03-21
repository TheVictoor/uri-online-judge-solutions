#include <stdio.h>

int main(){
	int i, j, x;
	i = 1;
	j = 7;

	while(i < 10){
		x = j - 3;
		for(; j > x; j--){
			printf("I=%d J=%d\n", i , j );
		}
		j += 5;
		i += 2;
	}	

	return 0;
}