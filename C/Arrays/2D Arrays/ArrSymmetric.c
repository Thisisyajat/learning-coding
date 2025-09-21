/*This program checks if the given matrix is symmetric or not.*/
#include <stdio.h>
#include <stdlib.h>

int main(){
    int m, n, i, j, isSym = 1;
    system("clear"); //for Windows : cls
    printf("Enter the order of the square matrix (e.g. 3 3 for 3x3 order) --> ");
    if (scanf("%d%d", &m, &n), m != n || (m < 2 || n < 2)) {
        printf("Given is not a square matrix.\nExiting...");
        exit(0);
    }
    float arr[n][n];
    printf("Enter %d elements of the matrix below, one in each line:\n", n*n);
    for (i = 0; i < n; i++) for (j = 0; j < n; j++) scanf("%g", &arr[i][j]);
    printf("\nEntered matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) printf("%g   ", arr[i][j]);
        printf("\n");
    }
    
    for (i = 0; i < n; i++) for (j = i + 1; j < n; j++) if (arr[i][j] != arr[j][i]) {
        isSym = 0;
        break;
    }
    if (isSym) printf("\nThe given matrix is symmetric.\nExiting...");
    else printf("\nThe given matrix is not symmetric.\nExiting...");
    return 0;
}