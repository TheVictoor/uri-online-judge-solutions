#include <stdio.h>

int main(){
	int x = 0;
	int v[1000];
	int a,b,c;

	scanf("%d", &x);


	for(c = 0; c < 1000; ){
		for(b = 0; b < x; b++){
			v[c] = b;
			c++;
			if(c == 1000) break;
		}
	}

	for(a = 0; a < 1000; a++){
		printf("N[%d] = %d\n", a , v[a]);
	}

}
