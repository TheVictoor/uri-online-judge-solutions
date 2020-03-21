#include <stdio.h>

int main(int argc, char const *argv[])
{
	
		int a = 0;
		int m = 0;
		int d = 0;

		int x = 0;

		int z = 0;

		scanf("%d" , &x);

		z = x / 365;

		if(z > 0){
			a = z;
			z = 0;
			x %= 365;
		}

		z = x / 30;

		if (z > 0)
		{
			m = z;
			z = 0;
			x %= 30;	
		}

		d = x;

		printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", a ,m , d );


	return 0;
}