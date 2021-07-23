#include <stdlib.h>
#include<stdio.h>
  
int main(int argc, char *argv[]) 
{
    float a, b;
	float sum, rest, div, mult;


    a = atoi(argv[1]); 
    b = atoi(argv[2]);

	sum= a+b;
	rest=a-b;
	mult=a*b;
	div=a/b;

    printf("The sum is: %.1f\n",sum);
	printf("The rest is: %.1f\n",rest);
	printf("The rest is: %.1f\n",mult);
	printf("The rest is: %.2f\n",div);
  

    return 0;
}