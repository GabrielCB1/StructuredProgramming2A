#include <stdio.h>
#include <stdlib.h>

int array [5];
int* arrayPointer = NULL;

int arreglo = NULL;

//char myChar = '9';//
//int oint = 9;//

int main(){

    //int myInt = myChar - '0';//
    //myChar = oint + '0';//

    arrayPointer = (int*) malloc(6* sizeof(int));

    for (int index =0; index<6; index++){

        printf ("arrayPointer[%d]: '%d'\n ", index, arrayPointer [index]);

    }

    arreglo = (int*) calloc (6, sizeof(int));
    for (int index = 0; index<6; index++)
    {
        printf ("arreglo [%d]: '%d'\n", index, arreglo[index]);
    }


    arrayPointer = (int*)realloc (arrayPointer,10);
    arrayPointer[6]= 20;
    arrayPointer[7]= 28;
    arrayPointer[8]= 25;
    arrayPointer[9]= 24;



    return 0;
}