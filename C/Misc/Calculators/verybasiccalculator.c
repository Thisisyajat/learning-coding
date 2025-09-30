#include <stdio.h>
#include <math.h>

int main(){
    float num1, num2,ans;
    char op,opval;
    printf("Welcome to the calculator!\nEnter first number --> ");
    scanf("%f",&num1);
    printf("Enter operator symbol --> ");
    scanf(" %c", &op);
    printf("Enter second number --> ");
    scanf("%f",&num2);
    switch (op)
    {
    case '+': ans = num1 + num2;
        break;
    case '-': ans = num1 - num2;
        break;
    case '*': ans = num1 * num2;
        break;
    case '/': ans = num1 / num2;
        break;
    case '^': ans = pow(num1,num2);
        break;
    case '%': ans = (int)num1 % (int)num2;
        break;
    default:
        break;
    }
    printf("\n%f %c %f = %f",num1,op,num2,ans);
    return 0;
}