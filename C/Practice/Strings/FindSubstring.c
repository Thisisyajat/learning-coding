#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    const int max = 100;
    char str[max], sub[max];
    int i = 0, j, count = 0, main_len, sub_len, found, pos[max];
    printf("Enter the main string below:\n");
    if (gets(str), str[0] == '\0'){
        printf("Main string cannot be empty.\nExiting...");
        exit(0);
    }
    printf("Enter the sub-string --> ");
    if (gets(sub), sub[0] == '\0'){
        printf("Substring cannot be empty.\nExiting...");
        exit(0);
    }
    main_len = strlen(str);
    sub_len = strlen(sub);
    while (i <= (main_len - sub_len)) {
        found = 1;
        for (j = 0; j < sub_len; j++) if (str[i + j] != sub[j]) {
            found = 0;
            break;
        }
        if (found) pos[count++] = i + 1;
        i++;
    }
    if (!count) printf("\n\"%s\" was not found in \"%s\".", sub, str);
    else {
        printf("\n\"%s\" was found %d time(s) in \"%s\" at positions: %d", sub, count, str, pos[0]);
        for (i = 1; i < count; i++) printf(", %d", pos[i]);
    }
    return 0;
}