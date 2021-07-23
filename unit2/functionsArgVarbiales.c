#include <stdio.h>
#include "./foldertest/utils.h"
#include <stdlib.h>

int var1 =10;
int var2 =20;

int myVar1 =30;
int myVar2=50;

int  main (int argc, char** argv){

    printf("var1 = %d, var2= %d\n", var1, var2);
    printf ("Function was executed.\n");

    //paso de argumentos por direccion
    modifyVariables (var1,var2);
    printf("var1 = %d, var2= %d\n", var1, var2);

    //Get address of var1 and var2
    // & = "la direccion de"
    int * myptr1 = &var1;
    int * myprt2 = &var2;

    printf("Address var1: %p,\t, address var2: %p\n", &var1, &var2);

    printf("Pointer address modified the var1: \n");
    *myptr1 = 20;
    var2 =40;


    // *myprt1 =  "El  valor de la direccion" >>
    modifyVaribalesAddress ( &var1, &var2);
    modifyVaribalesAddress ( &var1, &var2);   
    printf ("var1= %d, var2= %d\n",var1,var2);  

    //paso de argumentos por direccion 
    

return 0;
}