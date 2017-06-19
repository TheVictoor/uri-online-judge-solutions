#include <stdio.h>

int main(){
	float n1,n2,n3,n4,n5;
	double r, r2;
	n1 = n2 = n3 = n4 = n5 = 0.0;
	r = r2 = 0.0;

	scanf("%f %f %f %f", &n1 , &n2 , &n3 , &n4);

	r = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4 ) / 10;

	printf("Media: %.1lf\n", r);

	if(r >= 7.0){
		printf("Aluno aprovado.\n");

	}else if(r < 5.0){
		printf("Aluno reprovado.\n");

	}else {
		printf("Aluno em exame.\n");

		scanf("%f", &n5);
		printf("Nota do exame: %.1f\n", n5);

		r2 = (r + n5) / 2.0;

		if(r2 >= 5.0){
			printf("Aluno aprovado.\n");
		}else{
			printf("Aluno reprovado.\n");
		}
		printf("Media final: %.1lf\n", r2);

	}
	return 0;
}
