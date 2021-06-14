#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TAN 10

int lista [TAN] = {7,24,33,41,50,65,73,86,97,133};
int idx = 0;


typedef int INTEGER;

int main(int argc, char** argv){

    int index2=0;
    for (int index =1; index<=TAN; index++,index2++){
        printf ("index: %d, index2: %d\n\a",index, lista[index]);

        for (INTEGER i=0; i<3; i++){




        }




    }

    while ( true )
    {
        if (lista[idx]==50){
            break; 
        }
        /*code*/
        idx++;
    }
    printf ("idx found: %d", idx);


    int idx_for =0;
    for (; lista[idx_for] != 50; idx_for++ ){
        printf( "idx_for found: %d", idx_for);
    }

    return 0;
}