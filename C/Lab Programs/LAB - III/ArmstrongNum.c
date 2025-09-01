/*This program checks if the given 3-digit number is an Armstrong number.*/

#include <stdio.h>
#include <math.h>

int main(){
    int num, n, sum = 0, dig;
    printf("Enter a 3-digit number --> ");
    scanf("%d", &num);
    n = num;
    while (num != 0){
        dig = num % 10;
        sum += pow(dig,3);
        num /= 10;
    }
    if (sum == n) printf("\n%d is an Armstrong number.",n);
    else printf("\n%d is not an Armstrong number.",n);
    return 0;
}
