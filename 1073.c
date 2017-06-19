#include <stdio.h>
#include <math.h>

int main(){
	int n = 0, x = 0, z = 0;

	scanf("%d", &n);

	for(x = 1; x <= n; x++){
		if(x % 2 == 0){
			z = pow(x,2);
			printf("%d^2 = %d\n", x , z);
		}
	}

	return 0;

}