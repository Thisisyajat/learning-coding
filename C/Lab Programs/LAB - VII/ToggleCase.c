#include <stdio.h>

int main(){
    const int max = 100;
    char str[max];
    printf("Enter your string below:\n");
    gets(str);
    // toggle case
    for (int i = 0; str[i] != '\0'; i++) {
        //if (str[i] > 90 && str[i] < 97) printf("%c", str[i]);
        if (str[i] > 96 && str[i] < 123){
            str[i] -= 32;
            printf("%c", str[i]);
        }
        else if (str[i] < 91 && str[i] > 64){
            str[i] += 32;
            printf("%c", str[i]);
        }
        else printf("%c", str[i]);
    }
    return 0;
}