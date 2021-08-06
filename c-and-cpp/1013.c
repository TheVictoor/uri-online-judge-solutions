#include <stdio.h>

int main() {


	int x = 0;
	int c = 0;
	int v = 0;


	scanf("%d %d %d", &x, &c, &v);

	if(x > c && x > v){
		printf("%d eh o maior\n", x);
	}else if(c > x && c > v){
		printf("%d eh o maior\n", c);
	}else{
		printf("%d eh o maior\n", v);
	}

	return 0;
}