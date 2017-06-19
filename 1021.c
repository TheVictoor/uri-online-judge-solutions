#include <stdio.h>

int main(int argc, char const *argv[])
{

    double x = 0.0;
    int z = 0;

    z = 0;

    scanf("%lf", &x);

    printf("NOTAS:\n");
    while(x >= 100){
        z++;
        x -= 100;
    }
    printf("%d nota(s) de R$ 100.00\n", z);
    z = 0;

    while(x >= 50){
        z++;
        x -= 50.00;
    }
    printf("%d nota(s) de R$ 50.00\n", z);
    z = 0;

    while(x >= 20){
        z++;
        x -= 20;
    }
    printf("%d nota(s) de R$ 20.00\n", z);
    z = 0;

    while(x >= 10){
        z++;
        x -= 10;
    }
    printf("%d nota(s) de R$ 10.00\n", z);
    z = 0;

    while(x >= 5){
        z++;
        x -= 5;
    }
    printf("%d nota(s) de R$ 5.00\n", z);
    z = 0;

    while(x >= 2){
        z++;
        x -= 2;
    }
    printf("%d nota(s) de R$ 2.00\n", z);
    z = 0;


    printf("MOEDAS:\n");
    while(x >= 1){
        z++;
        x -= 1;
    }
    printf("%d moeda(s) de R$ 1.00\n", z);
    z = 0;


    x*= 100;

    while(x >= 50){
        z++;
        x -= 50;
    }
    printf("%d moeda(s) de R$ 0.50\n", z);
    z = 0;


    while(x >= 25){
        z++;
        x -= 25;
    }
    printf("%d moeda(s) de R$ 0.25\n", z);
    z = 0;


    while(x >= 10){
        z++;
        x -= 10;
    }
    printf("%d moeda(s) de R$ 0.10\n", z);
    z = 0;


    while(x >= 5){
        z++;
        x -= 5;
    }
    printf("%d moeda(s) de R$ 0.05\n", z);
    z = 0;

    while(x >= 1){
        z++;
        x -= 1;
    }

    printf("%d moeda(s) de R$ 0.01\n", z);
    z = 0;


	return 0;
}
