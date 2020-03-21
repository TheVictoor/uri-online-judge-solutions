#include <stdio.h>

int main(){
	float s = 0.0;

	float x = 0.0;

	scanf("%f", &s);

	if(s <= 2000.00){
		printf("Isento\n");
		return 0;
	}else{
		if(s <= 3000){
			x = (s - 2000) * 0.08;
		}else if(s <= 4500){
			x = 1000 * 0.08;
			x += (s - 3000.00) * 0.18;
		}else{
			x = 1000 * 0.08;
			x += 1500 * 0.18;
			x += (s - 4500) * 0.28;
		}

		printf("R$ %.2f\n", x);
	}

	return 0;
}