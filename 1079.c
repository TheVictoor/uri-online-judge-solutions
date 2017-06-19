#include <stdio.h>

int main(){
	int n, x;
	float n1, n2, n3, m;
	int p1, p2, p3;

	n1 = n2 = n3 = m = 0;
	p1 = 2; 
	p2 = 3; 
	p3 = 5;
	n = 0;

	scanf("%d", &n);

	for(x = 0; x < n; x++){
		scanf("%f %f %f", &n1, &n2, &n3);
		m = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3);
		printf("%.1f\n", m);
	}

	return 0;
}