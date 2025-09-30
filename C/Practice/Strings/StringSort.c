#include <stdio.h>
#include <string.h>

int main(){
    const int max = 50;
    int i, j, n;
    printf("Enter number of names --> ");
    scanf("%d", &n);
    char str[n][max], temp[max];
    printf("Enter names, one in each line below:\n");
    for (i = 0; i < n; i++) scanf("%s", str[i]);
    for (i = 0; i < n - 1; i++) for (j = i + 1; j < n; j++) if (strcmp(str[i], str[j]) > 0) {
        strcpy(temp, str[i]);
        strcpy(str[i], str[j]);
        strcpy(str[j], temp);
    }
    printf("\nSorted names:\n");
    for (i = 0; i < n; i++) printf("%s\n", str[i]);
    return 0;
}