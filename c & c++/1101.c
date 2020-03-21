#include <stdio.h>

int main(){
	int x , y;
	x = y =  0;

	while(1){
		scanf("%d %d", &x , &y);
		if(x <= 0 || y <= 0 )
			break;

		int m, n, s;
		s = 0;

		n = x > y ? y : x ;
		m = x < y ? y : x ;

		for(; n <= m; n++){
			printf("%d ", n);
			s += n;
		}

		printf("Sum=%d\n", s);

	}


}