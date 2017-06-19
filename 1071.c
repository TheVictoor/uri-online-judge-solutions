#include <stdio.h>

int main(){
	int x, y;
	int s, n, m;

	s = 0;

	scanf("%d %d", &x , &y);

	m = x > y ? x : y;
	n = x < y ? x : y;

	n++;

	for( ; n < m ; n++){
		if(n % 2 == 1 || n % 2 == -1){
			s += n;
		}
	}

	printf("%d\n", s);

	return 0;

}