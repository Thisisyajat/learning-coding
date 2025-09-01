/*Program to calculate roots of a quadratic equation.*/

#include <stdio.h>
#include <math.h>

int main(){
    float a, b, c, disc, root1, root2, re, im;
    int d;
    printf("Enter a, b, c of a quadratic equation of format ax^2 + bx + c = 0, a != 0 --> ");
    scanf("%f%f%f", &a, &b, &c);
    disc = (b * b) - (4 * a * c);
    if (disc < 0) d = 1;
    else if (disc == 0) d = 2;
    else d = 3;
    switch (d){
    case 1:
        re = (-b)/(2*a);
        im = (pow(-disc, 0.5))/(2*a);
        printf("Real root --> %f , Imaginary root --> %f\n%f + i(%f)",re, im, re, im);
        break;
    case 2:
        re = (-b)/(2*a);
        printf("Both roots are equal --> %f", re);
        break;
    case 3:
        root1 = (-b + pow(disc,0.5))/(2 * a);
        root2 = (-b - pow(disc,0.5))/(2 * a);
        printf("Root 1 --> %f\nRoot 2 --> %f",root1, root2);
        break;
    default: break;}
    return 0;
}
