#include <stdio.h>
#include <stdlib.h>

int Prime(int n){
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
    printf("Enter the limit of the prime series --> ");
    if (scanf("%d", &n), n < 1){
        printf("Entered number cannot be less than 1.\nExiting...");
        exit(0);
    }
    for (int i = 2; i <= n; i++)  if (Prime(i)) printf("%d  ", i);
    return 0;
}