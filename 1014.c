#include <stdio.h>

int main(int argc, char const *argv[])
{
	//entradas
	int km = 0;
	float comb  = 0.0;

	//variavel para receber resultado	
	float r = 0;

	//ler os dois valores 
	scanf("%d", &km);
	scanf("%f" , &comb);

	//fazer a operacao e atribuir a r
	r = km / comb;

	//exebir o resultado com 3 casas decimais
	printf("%.3f km/l\n", r );


	return 0;
}