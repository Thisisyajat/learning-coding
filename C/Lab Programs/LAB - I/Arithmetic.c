#include <stdio.h>

int main(){
    float num1,num2,sum,diff,prod,quo;
    printf("This program takes two numbers and displays their sum, difference, product and quotient.\nEnter first and second number --> ");
    scanf("%f%f",&num1,&num2);
    sum = num1+num2;
    diff = num1-num2;
    prod = num1*num2;
    quo = num1/num2;
    printf("\nSum --> %f + %f = %f\nDifference --> %f - %f = %f\nProduct --> %f * %f = %f\nQuotient --> %f / %f = %f\n",num1,num2,sum,num1,num2,diff,num1,num2,prod,num1,num2,quo);
    return 0;
}
