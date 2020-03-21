#include <stdio.h>

int main(){
	int tot, sap, rat, coe, n, x, a;
	tot = sap = rat = coe = n = a = 0; 

	double p = 0.0;
	
	char y;

	scanf("%d", &n);

	for(x = 0; x < n; x++){
		scanf("%d %c", &a, &y);
		if(y == 'C'){
			coe += a;
		}else if(y == 'S'){
			sap += a;
		}else if(y == 'R'){
			rat += a;
		}
	}

	tot = rat + sap + coe;

	printf("Total: %d cobaias\n", tot);
	printf("Total de coelhos: %d\n", coe);
	printf("Total de ratos: %d\n", rat );
	printf("Total de sapos: %d\n", sap);

	p = (coe * 100.0)/tot;
	printf("Percentual de coelhos: %.2lf %%\n", p );

	p = (rat * 100.0)/tot;
	printf("Percentual de ratos: %.2lf %%\n", p);

	p =  (sap * 100.0)/tot;
	printf("Percentual de sapos: %.2lf %%\n", p);

	return 0;
}