/*Strings practice*/

#include <stdio.h>
#include <string.h>
#include <math.h>

void printString(char arr[]);

int main() {
    char str[100];
    char str1[100];
    //har str2[] = "";
    char salt[] = "chee";
    int len;
    printf("Enter your password --> ");
    fgets(str, 200, stdin);
    printf("%s\n", str);
    for (int i = 0; i < (floor(strlen(str)/2)); i++){
        strcat(str1, str[i]);
    }
    strcat(str1,salt);
    for (int i = (floor(strlen(str)/2)); i <= strlen(str)/2; i++){
        strcat(str1, str[i]);
    }
    puts(str1);
}

void printString(char arr[]){
    for (int i = 0; arr[i] != '\0'; i++){
        printf("%c", arr[i]);
    }
}