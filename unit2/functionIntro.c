#include <stdio.h>

int myNumber = 3;
float myFloat = 3.1416;
char myString [255] = "Hola mundo";


//declare and defined

void sayHello (char message[]){
    printf ( "%s\n", message );
}

void sayMyName (char message[]);

int main () {

    sayHello ("Hello world");
    sayMyName ("Gabriel");
    return 0;
}

void sayHello (char message[]){
    printf ( "%s\n", message );
   