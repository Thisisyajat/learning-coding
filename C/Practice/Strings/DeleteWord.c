#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    const int max = 1000;
    char str[max], word[max];
    int count = 1, n = 0, i = 0, j = 0, r = 0;
    printf("Enter your sentence below:\n");
    if (gets(str), str[0] == '\0'){
        printf("Sentence cannot be empty.\nExiting...");
        exit(0);
    }
    printf("Enter your word to delete below:\n");
    if (gets(word), word[0] == '\0'){
        printf("Word cannot be empty.\nExiting...");
        exit(0);
    }

    // counting words
    for (int i = 0; str[i] != '\0'; i++) if (str[i] == ' ' && str[i + 1] != ' ') count++;
    char words[count][50];

    // breaking sentence into words, and appending to an array
    for (int i = 0; str[i] != '\0'; i++){
        if (str[i] != ' ') words[n][j++] = str[i];
        else {
            words[n][j++] = '\0';
            n++, j = 0;
        }
    }
    
    int write = 0;
    for (int i = 0; i < n; ++i) if (strcmp(words[i], word) != 0) {
            if (write != i) strcpy(words[write], words[i]);
            write++;
        }

    printf("\nEdited sentence:\n");
    for (int i = 0; i < write; i++) printf("%s ", words[i]);
    printf("\n");
    return 0;
}