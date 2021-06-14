#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TAN 10

int lista [TAN] = {7,24,33,41,50,65,73,86,97,133};
int idx = 0;

typedef int INTEGER;

int main(int argc, char** argv){

    int index2=0;
    for (int index =0; index<=TAN; index++,index2++){
        printf ("index: %d, index2: %d\n\a",index, lista[index]);

        for (size_t i=0; i<3; i++){

            printf ("Hola Mundo!\n");

        }
    }

  
    return 0;
}


