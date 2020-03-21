#include <stdio.h>

int main(int argc, char const *argv[])
{
	int x = 0;
	int c = 0;

	scanf("%d" , &x);
	scanf("%d" , &c);

	float l = (x * c) / 12.0;

	printf("%.3f\n", l);
	
	return 0;
}