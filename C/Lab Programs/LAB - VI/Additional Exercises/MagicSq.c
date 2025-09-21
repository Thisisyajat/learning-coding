/*This program checks whether the given matrix is magic square or not.*/
#include <stdio.h>
#include <stdlib.h>

int main(){
    int m, n, i, j, magicConst;
    system("clear"); //for Windows : cls
    printf("Enter the order of the square matrix (e.g. 3 3 for 3x3 order) --> ");
    if (scanf("%d%d", &m, &n), m != n || (m < 2 || n < 2)) {
        printf("Given is not a square matrix.\nExiting...");
        exit(0);
    }
    float arr[n][n], sum;
    printf("Enter %d elements of the matrix below, one in each line:\n", n*n);
    for (i = 0; i < n; i++) for (j = 0; j < n; j++) scanf("%g", &arr[i][j]);
    printf("\nEntered matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) printf("%g\t", arr[i][j]);
        printf("\n");
    }
    magicConst = (n * (n * n + 1)) / 2;
    // row sum
    for (i = 0; i < n; i++) {
        sum = 0;
        for (j = 0; j < n; j++) sum += arr[i][j];
        if (sum != magicConst) {
            printf("\nNot a magic square.\nExiting...");
            exit(0);
        }
    }
    // column sum
    for (j = 0; j < n; j++) {
        sum = 0;
        for (i = 0; i < n; i++) sum += arr[i][j];
        if (sum != magicConst) {
            printf("\nNot a magic square.\nExiting...");
            exit(0);
        }
    }

    //primary diagonal sum
    sum = 0;
    for (i = 0; i < n; i++) sum += arr[i][i];
    if (sum != magicConst) {
    printf("\nNot a magic square.\nExiting...");
    exit(0);
    }

    //secondary diagonal sum
    for (i = 0; i < n; i++){
        sum = 0;
        for (j = n - 1; j > -1; j--) sum += arr[i][j];
        if (sum != magicConst) {
            printf("\nNot a magic square.\nExiting...");
            exit(0);
        }
    }

    printf("\nThe given square matrix is a Magic Square!\n");
    return 0;
}