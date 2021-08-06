#include <stdio.h>

int main(){
	int a[3] = {0 , 0 , 0};
	int b[3] = {0 , 0 , 0};
	int x = 0;
	int j, i;

	
	scanf("%d %d %d", &b[0], &b[1] , &b[2]);

	a[0] = b[0];
	a[1] = b[1];
	a[2] = b[2];

	for (j = 0; j < 2; j++)
	{
		for (i = 0; i < 2; i++)
		{
			if(a[i] > a[i+1]){
				x = a[i+1];
				a[i+1] = a[i];
				a[i] = x;
			}		
		}
	}

	printf("%d\n%d\n%d\n",a[0], a[1], a[2]);
	printf("\n%d\n%d\n%d\n",b[0], b[1], b[2] );

	return 0;
}
