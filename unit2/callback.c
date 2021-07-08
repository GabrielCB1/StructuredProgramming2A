#include <stdio.h>
#include <string.h>
#include "./foldertest/utils.h"
#include "stdbool.h"




void callToNumber(int number){
    //Logica completa para llamar a un numero//
    printf ("Llamando al %d...!\n", number);
}

void sendMessageToNumber(int number){
    //Complex logic to send a msg//
    printf ("sending sms to %d...!\n", number);
}

void SecurityCamera ( void (*cb) (int number), int EmergencyNumber );

int main(){

    for (;;){
        SecurityCamera (callToNumber, 911);
        SecurityCamera (sendMessageToNumber, 911);
    }
    

    return 0;
}


void SecurityCamera ( void (*cb) (int number), int EmergencyNumber ){
    //logica compleja//
    bool thief = true;
    if (thief){ //Si detecta a un ladron debe hacer algo!//
    //ejectura un callback//
    cb (EmergencyNumber);


    }
}

void SecurityCamera2(){

    callToNumber(999);
}