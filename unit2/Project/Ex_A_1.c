#include<stdio.h>
#include<stdlib.h>
  
void main(int argc, char * argv[]) {

    int i, ave = 0;
    float tot;
 
    printf("The average is: ");

    for (i = 1; i < argc; i++){
        ave = ave + atoi(argv[i]);
      }       
    argc = argc - 1;
    tot = ave / argc;
    printf("%.2f\n",tot);

}