// This program finds the factorial of a given number using a function. Using this function, compute NCR in the main function.

#include <stdio.h>

int fact(int n){
    if (n <= 1) {
        return 1;
    }
    return n * fact(n-1);
}

int main(){
    int n, r;
    printf("Enter n and r of nCr --> ");
    scanf("%d %d", &n, &r);
    printf("\n%dC%d = %d", n, r, fact(n)/((fact(n - r))*(fact(r))));
}