//Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

#include <stdio.h>
#include <math.h>

int main(){

	float a,b,c,d,r1,r2;

	a=b=c=d=r1=r2=0.0;

	scanf("%f %f %f", &a , &b, &c);

	d = pow(b,2) - (4 * a * c);

	if(d <= 0 || a == 0){
		printf("Impossivel calcular\n");
		return 0;
	}

	
	r1 = (-b + sqrt(d))/(2*a);
	r2 = (-b - sqrt(d))/(2*a);

	printf("R1 = %.5f\nR2 = %.5f\n", r1, r2 );

	return 0;
}