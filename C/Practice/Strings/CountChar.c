/*Count the characters in an entered string.*/

#include <stdio.h>

int main(){
    const int max = 100;
    char str[max];
    int count = 0, i = 0;
    printf("Enter a string --> ");
    str[max] = gets(str);   //unsafe
    printf("Entered string:\n");
    puts(str);
    while (str[i] != '\0')
    {
        count++, i++;
    }
    printf("\nThe count is --> %d\n", count);
    return 0;
}