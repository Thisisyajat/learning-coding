#include <stdio.h>
const int max = 1000;
int i = 0, count = 0;
void option1();
void option2();

int main(){
    printf("Enter string below (\"enter # when done in a new line\"):\n");
    option1();
    //option2();
    return 0;
}

void option1(){
    char str[max];
    scanf("%[^#]",str);
    printf("Entered string:\n");
    puts(str);
    for (i = 0; str[i] != '\0'; i++) {
        count++;
    }
    printf("\nThe count is --> %d\n", count);
}

void option2(){
    char str[max];
    fgets(str, max, stdin);
    printf("Entered string:\n");
    puts(str);
    while (str[i] != '\0') count++, i++;
}