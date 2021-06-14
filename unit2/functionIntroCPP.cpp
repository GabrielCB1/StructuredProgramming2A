#include <iostream>
#include <tuple>

std::string myString = "hola mundo";
int myNumber = 3;
float myFloat = 3.1416;

std::tuple<int,int> myTuple = {1,2};

void sayHello (std::string tag1);

int main (){

    sayHello (myString);

    return EXIT_SUCCESS;

}

void sayHello (std::string tag1){

    std::cout<<tag1<<std::endl;

}