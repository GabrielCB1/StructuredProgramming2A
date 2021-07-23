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
    arrayPointer[0]= 35;
    arrayPointer[1]= 36;
    arrayPointer[2]= 37;
    arrayPointer[3]= 39;
    arrayPointer[4]= 40;
    arrayPointer[5]= 41;
    

    for (int index =0; index<6; index++){

        printf ("arrayPointer[%d]: '%d'\n ", index, arrayPointer [index]);

    }

    arreglo = (int*) calloc (6, sizeof(int));
    for (int index = 0; index<6; index++)
    {
        printf ("arreglo [%d]: '%d'\n", index, arreglo[index]);
    }


    arrayPointer = realloc (arrayPointer,10*sizeof(int));
    arrayPointer[6]= 20;
    arrayPointer[7]= 28;
    arrayPointer[8]= 25;
    arrayPointer[9]= 24;

    printf("------------\n");
    for (int index= 0; index<10; index++)
    {
        printf("arrayPointer[%d]:'%d'\n", index, arrayPointer[index]);
    }
    
    free(arrayPointer);



    return 0;
}