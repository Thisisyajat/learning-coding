#include <stdio.h>
#include <stdlib.h>

int fibonacci(int n) {
    int i = 1, j = 0, next;
    printf("%d  %d  ", j, i);
    while (j <= n) {
        next = j + i;
        printf("%d  ", next);
        j = i;
        i = next;
    }
}

int main(){
    int n;
    printf("Enter limit number to generate Fibonacci series --> ");
    if (scanf("%d", &n), n < 1) {
        printf("Enter a valid limit.\nExiting...");
        exit(0);
    }
    fibonacci(n);
}