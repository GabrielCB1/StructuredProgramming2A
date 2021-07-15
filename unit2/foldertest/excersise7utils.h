#include <stdio.h>
#include <stdlib.h>

typedef struct Robot{
    char *name;
    char *type;
    float height;
    float weight;
    float degreesOfFreedom;
    void (*sayHelloToRobot) (struct Robot);
}ROBOT;

/*ROBOT markovito = {"Markovito", "ServiceRobot", 1.2, 2.5, 3};
ROBOT tiago = {"Tiago", "ServiceRobot", 1.7, 2.8, 7 };*/





void sayHelloToRobot( ROBOT robot_x  ){
        
        printf(  "\n %s %s \n ", "hola mundo ",robot_x.name);
}
