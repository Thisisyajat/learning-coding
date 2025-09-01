#include <stdio.h>

int main(){
    float cm, in;
    printf("This program converts inches to cm.\n");
    printf("Enter a number (in inches) --> ");
    scanf("%f",&in);
    cm = in * 2.54;
    printf("%f inches is equivalent to %f centimeters.\n",in,cm);
    return 0;
}
