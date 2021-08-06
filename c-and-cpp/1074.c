#include <stdio.h>

int main(){
	int x, v, c;
	x = v = c = 0;

	scanf("%d", &c);

	for(x = 0; x < c; x++){
		scanf("%d", &v);
		if(v % 2 == 0){
			if(v == 0){
				printf("NULL\n");
			}else if(v > 0){
				printf("EVEN POSITIVE\n");
			}else{
				printf("EVEN NEGATIVE\n");
			}
		}else {
			if(v > 0){
				printf("ODD POSITIVE\n");
			}else{
				printf("ODD NEGATIVE\n");
			}
		}
	}	

	return 0;
}