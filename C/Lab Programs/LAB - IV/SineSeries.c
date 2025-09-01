#include <stdio.h>
#include <math.h>
//float rad(float angle);

int main(){
    int n;
    float x, term, sum;
    printf("Enter the terms and angle (in deg) --> ");
    scanf("%d%f", &n, &x);
    x *= (3.1416)/180;
    //x = rad(x);
    term = sum = x;
    for (int i = 1; i < n; i++)
    {
        term *= (((-1) * x * x)/(2 * i * (2 * i + 1)));
        sum += term;
    }
    printf("\nThe library value of sin(%f) = %f", x, sin(x));
    printf("\nThe computed value of sin(%f) = %f", x, sum);
    return 0;
}

/*float rad(float angle){
    return angle * (3.1418)/180;
}*/