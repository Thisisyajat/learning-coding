#include <stdio.h>
#include <math.h>
float addition();
float subtraction();
float multiplication();
float division();
float exp();
float num1,num2;
char mode;
int count;

void main(){
    printf("Welcome to the calculator!");
    printf("\nEnter number %d --> ",count);
    scanf("\n%f",&num1);
    while ((getchar()) != '\n');
    printf("\nPlease select an operation:\n     - Addition (type +)\n     - Subtraction (type -)\n     - Multiplication (type *)\n     - Division (type /)\n     - Raise to power (type ^)\n     - Modulo (type \%) \n     - Exit (type e)\n\nYour response --> ");
    scanf("%c",&mode);
    if (mode == 'e')
    {
        printf("\nBye bye...");
        return;
    }  
    count++;
    printf("Enter number %d --> ",count);
    scanf("%f",&num2);
    
}

float addition(){}
float subtraction(){}
float multiplication(){}
float division(){}
float exp(){}