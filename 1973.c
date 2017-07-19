#include <stdio.h>

int main(){

	long long int atk = 1;
	long long int p = 0;
	long long int q = 0;
	long long int i = 0;

	long long int estrelas = 0;
	scanf("%lld", &estrelas);

	long long int carn[estrelas];

	for(i = 0; i < estrelas; i++) {
		scanf("%lld", &carn[i]);
	}
	while(1){
		if(p < 0 || p == estrelas){
			break;
		}else if(carn[p] % 2 == 0){
			if(carn[p] > 0){
				carn[p] -= 1;
			}
			p -= 1;
		}else if(carn[p] % 2 == 1){
			if(carn[p] > 0){
				carn[p] -= 1;
			}
			p += 1;
			atk += 1;
		}
	}

	for(i = 0; i < estrelas; i++){
		q += carn[i];
	}

	if(p < 0){
		printf("%lld %lld\n", atk , q );
	}else if(p >= estrelas){
		printf("%lld %lld\n", atk - 1, q );
	}

	return 0;

}