#include <stdio.h>

int main(int argc, char const *argv[])
{
	
	int h = 0;
	int m = 0;
	int s = 0;

	int x = 0;

	int z = 0;


	scanf("%d" , &x);

	z = x / 3600;

	if(z > 0){
		h = z;
		z = 0;
		x %= 3600;
	}

	z = x / 60;

	if(z > 0){
		m = z;
		z = 0;
		x %= 60;
	}

	s = x;

	printf("%d:%d:%d\n", h, m, s);
	
	return 0;
}