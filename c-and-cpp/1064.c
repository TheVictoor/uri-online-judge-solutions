#include <stdio.h>

int main(){
	int x, c;
	float m, v, s;
	m = v = s = 0;
	c = x  = 0;	

	for (x = 0; x < 6; x++){
		scanf("%f", &v);
		if(v > 0){
			c++;
			s += v;
		}
	}

	m = s / c;

	printf("%d valores positivos\n%.1f\n", c, m);

	return 0;
}