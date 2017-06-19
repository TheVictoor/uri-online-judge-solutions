#include <stdio.h>
 
int main() {
	int par[5]; 
	int impar[5];
	
	int ci = 0;
	int cp = 0;
	int x = 0;
	int z = 0;
	int v;
	
	for(z =0; z < 15; z++){
		scanf("%d", &v);
		
		if(v % 2 == 1 || v % 2 == -1){
			if(ci == 5){
				for(x = 0; x < 5;x++){
					printf("impar[%d] = %d\n", x,  impar[x]);	
				}
				for(x = 0; x < 5; x++){
					impar[x] = 0;	
				}
				ci = 0;
				
				impar[ci] = v;
				
				ci++;
			}else{
				impar[ci] = v;
				
				ci++;
			}
			
		}else{
			if(cp == 5){
				for(x = 0; x < 5;x++){
					printf("par[%d] = %d\n", x,  par[x]);	
				}
				for(x = 0; x < 5; x++){
					par[x] = 0;	
				}
				cp = 0;
				
				par[cp] = v;
				
				cp++;
			}else{
				par[cp] = v;
				cp++;
			}
		}
	}
	
	for(z = 0; z < ci; z++){
		printf("impar[%d] = %d\n", z,  impar[z]);	
	}
	for(z = 0; z < cp; z++){
		printf("par[%d] = %d\n", z,  par[z]);
	}
	
    return 0;
}