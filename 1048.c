#include <stdio.h>

int main(){
	float sal = 0;
	float nsal = 0;
	int perc = 0;


	scanf("%f", &sal);

	if(sal <= 400){
		perc = 15;
		nsal = sal + ((sal * perc) / 100);
	}else if(sal <= 800.00){
		perc = 12;
		nsal = sal + ((sal * perc) / 100);
	}else if(sal <= 1200.00){
		perc = 10;
		nsal = sal + ((sal * perc) / 100);
	}else if(sal <= 2000.00){
		perc = 7;
		nsal = sal + ((sal * perc) / 100);
	}else{
		perc = 4;
		nsal = sal + ((sal * perc) / 100);
	}

	printf("Novo salario: %.2f\n", nsal );
	printf("Reajuste ganho: %.2f\n", nsal - sal );
	printf("Em percentual: %d %%\n", perc);

	return 0;
}