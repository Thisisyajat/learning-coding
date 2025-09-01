#include <stdio.h>
#include <math.h>

int main(){
    float p,r,n;
    printf("Enter principal amount, rate, and time period (years) --> ");
    scanf("%f%f%f",&p,&r,&n);
    printf("\nSimple interest = %.2f",(p*r*n)/100);
    printf("\nCompound interest = %.2f", (p * pow((1 + (r/100)),n)) - p);
    return 0;
}
