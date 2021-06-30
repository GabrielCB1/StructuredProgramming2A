#include <stdio.h>
/* Homework 2 using structure with C */
 

struct StudentData{
    char *name;
    int id;
    int age;
    int semester;
};
int main()
{
     /* student is the variable of structure StudentData*/
     struct StudentData student;

     /*Assigning the values of each struct member here*/
     student.name = "Gabriel Chuc";
     student.id = 2009150;
     student.age = 20;
     student.semester = 2;

     /* showing in screen the values of the student */
     printf("Student Name is: %s \n", student.name);
     printf("Student Id is: %d \n", student.id);
     printf("Student Age is: %d \n", student.age);
     printf("Student semester is: %d \n", student.semester);
     /*printf("\n");*/
     return 0;
}