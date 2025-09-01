/*Program to find the largest number among the given 3 numbers.*/
#include <stdio.h>

int main(){
    float num1,num2,num3;
    printf("Enter 3 numbers --> ");
    scanf("%f%f%f",&num1,&num2,&num3);
    if (num1 > num2){
        if (num1 > num3) printf("%f is the largest among the 3 given numbers.",num1);
        else printf("%f is the largest among the 3 given numbers.",num3);
    } else {
        if (num2 > num3) printf("%f is the largest among the 3 given numbers.",num2);
        else printf("%f is the largest among the 3 given numbers.",num3);
    }
    return 0;
}
