// This program uses a function IsPalin to check whether the given string is a palindrome or not. It also uses a main function to test this function.

#include <stdio.h>
#include <string.h>

int max = 100;
int isPalin(char str[max]){
    int len = strlen(str);
    for (int i = 0; i < len; i++) if (str[i] != str[len - 1 - i]) {
        return 0;
        break;
    }
    return 1;
}

int main(){
    char str[max];
    printf("Enter your string (max %d char): ", max);
    gets(str);
    int cond = isPalin(str);
    if (cond) printf("\nYes, it is a palindrome.");
    else printf("\nNo, it is not a palindrome.");
    return 0;
}