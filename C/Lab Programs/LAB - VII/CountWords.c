#include <stdio.h>

int main(){
    const int max = 100;
    char str[max];
    int i = 0, count = 1;
    printf("Enter your string below:\n");
    gets(str);
    while (str[i] != '\0'){
        if (str[i] == ' ' && str[i + 1] != ' ') count++;
        i++;
    }
    printf("\nNumber of words in the given string = %d", count);
    return 0;
}