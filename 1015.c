#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{

	float x1 = 0.0;
	float y1 = 0.0;
	float x2 = 0.0;
	float y2 = 0.0;

	float r = 0.0;
	float z = 0.0;

	scanf(" %f %f", &x1, &y1);
	scanf(" %f %f", &x2, &y2);

   printf("%f %f %f %f ", x1 , y1 , x2, y2);

	z = pow((x2 - x1), 2) + pow((y2 - y1),2);



	printf("%.4f\n", sqrt(z));

	return 0;
}
