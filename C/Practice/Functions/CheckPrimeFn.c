#include <stdio.h>
#include <stdlib.h>

int isPrime(int n){
    if (n <= 1) return 0;
    for (int i = 2; i <= n/2; i++){
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main(){
    int n;
    printf("Enter a number to check if it is a prime number --> ");
    if (scanf("%d", &n), n < 1) {
        printf("Entered number cannot be less than one.\nExiting...");
        exit(0);
    }
    if (isPrime(n)) printf("%d is a prime number.\nExiting...", n);
    else printf("%d is not a prime number.\nExiting...", n);
}