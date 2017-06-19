#include <stdio.h>
#include <math.h>

int main(){
	double d[3] = {0 , 0 , 0};
	double x;
	int j, i;

	double a, b, c;
	
	scanf("%lf %lf %lf", &d[0], &d[1] , &d[2]);

	for (j = 0; j < 2; j++)
	{
		for (i = 0; i < 2; i++)
		{
			if(d[i] < d[i+1]){
				x = d[i+1];
				d[i+1] = d[i];
				d[i] = x;
			}		
		}
	}

	a = d[0];
	b = d[1];
	c = d[2];

	

	if(a >= (b + c)){
		printf("NAO FORMA TRIANGULO\n");
		return 0;
	}else if(pow(a,2) == pow(b,2) + pow(c,2)){
		printf("TRIANGULO RETANGULO\n");
	}else if(pow(a,2) > pow(b,2) + pow(c,2)){
		printf("TRIANGULO OBTUSANGULO\n");
	}else if(pow(a,2) < pow(b,2) + pow(c,2)){
		printf("TRIANGULO ACUTANGULO\n");
	}

	if( a == b && b == c){
		printf("TRIANGULO EQUILATERO\n");
	}else if (a == b || b == c || a == c){
		printf("TRIANGULO ISOSCELES\n");
	}

	return 0;
}
