#include <stdio.h>
#include <stdlib.h> //atoi, atof
#include <string.h> // strcpy


int my_int= 12; // %i or %d
float my_float= 3.14; //%f
char my_char = 'c'; //%c
char my_str [10] = "Hola"; // $s


// POINTER 

int* my_ptr_int= &my_int; //p


int main ( int argc, char** argv){
    
    strcpy(my_str, argv[1]);
    int base = atoi(  my_str );

    strcpy(my_str, argv[2]);
    int altura = atoi(  my_str );
   
    printf ("my_int: %i, my_float: %f, my_char: %c, my_str: %s, my_prt_int: %p \n", my_int, my_float, my_char, my_str, my_ptr_int );
    printf ("argc: %i, element 1: %d, element 2: %s, char: %c \n", argc, base * altura ,argv[2], 'L'   ); //arg

    return 0;
}