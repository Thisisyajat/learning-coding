/*This program generates prime numbers between two given limits.*/

#include <stdio.h>

int main(){
    int lower, upper, prime, i, j;
    printf("Enter lower and upper limits --> "); // 1 15
    scanf("%d%d",&lower, &upper);
    printf("\nPrime number(s) between %d and %d are:\n", lower, upper);
    if (lower < 2) lower = 2; // lower = 2, upper = 15
    i = lower; // i = 2
    while (i <= upper){     // i <= 15
        prime = 1;
        j = 2;
        while (j <= i/2){
               if (i % j == 0){
                prime = 0;
                break;
               }
               j++;
        }
        if (prime) printf("%d\t",i);
        i++;
    }
    return 0;
}
