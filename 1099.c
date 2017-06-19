#include <stdio.h>

int main(){
	int a, b, c, x, y, me, ma, s;
	a = b = c =  x = y = me = ma = 0;

	scanf("%d", &a);

	for(x = 0; x < a; x++){
		s = 0;
		scanf("%d %d", &b , &c);
		me = b > c ? c : b;
		ma = b < c ? c : b;
		me++;
		for( ; me < ma; me++){
			if(me % 2 == 1){
				s += me;
			}
		}
		printf("%d\n", s);
	}	

	return 0;
}