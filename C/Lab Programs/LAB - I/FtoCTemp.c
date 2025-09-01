#include <stdio.h>

int main(){
    float f;
    printf("Enter temperature in Fahrenheit --> ");
    scanf("%f",&f);
    printf("\n%f F --> %f C",f,(5*(f-32))/9);
    return 0;
}
