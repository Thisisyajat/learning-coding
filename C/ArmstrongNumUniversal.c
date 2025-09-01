/*Program to check if the given number is an Armstrong number.
----------------------------WIP------------------------------*/

#include <stdio.h>
int power(int base, int exp);

int power(int base, int exp) {
    int result = 1;
    for(int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

int main(){
    int num, n, count = 0, dig, sum = 0;
    printf("Enter a number --> ");
    scanf("%d",&num);
    n = num;
    while (num != 0)
    {
        dig = num % 10;
        num /= 10;
        count++;
    }
    dig = 0;
    printf("\n%d\n", count);
    num = n;
    while (num != 0)
    {
        dig = num % 10;
        sum += power(dig,count);
        printf("%d\n", sum);
        num /= 10;
    }
    if (sum == n) printf("\n%d is an Armstrong number.",sum);
    else printf("\n%d is not an Armstrong number.",n);
    return 0;
}