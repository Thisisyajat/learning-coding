/*This program performs matrix multiplication.*/
#include <stdio.h>
#include <stdlib.h>

int main(){
    int r1, c1, r2, c2, i, j, k;
    system("clear"); //for Windows : cls
    printf("Enter the order of the first matrix A (e.g. 3 3 for 3x3 order) --> ");
    if (scanf("%d%d", &r1, &c1), r1 < 1 || c1 < 1) {
        printf("Invalid matrix order.\nExiting...");
        exit(0);
    }
    float arr1[r1][c1];
    printf("Enter %d elements of the matrix below, one in each line:\n", r1*c1);
    for (i = 0; i < r1; i++) for (j = 0; j < c1; j++) scanf("%f", &arr1[i][j]);
    printf("\nEntered matrix:\n");
    for (i = 0; i < r1; i++) {
        for (j = 0; j < c1; j++) printf("%g   ", arr1[i][j]);
        printf("\n");
    }
    printf("Enter the order of the second matrix B (e.g. 3 3 for 3x3 order) --> ");
    if (scanf("%d%d", &r2, &c2), (r2 < 1 || c2 < 1) || (r2 != c1)) {
        printf("Invalid matrix order.\nExiting...");
        exit(0);
    }
    float arr2[r2][c2];
    printf("Enter %d elements of the matrix below, one in each line:\n", r2*c2);
    for (i = 0; i < r2; i++) for (j = 0; j < c2; j++) scanf("%f", &arr2[i][j]);

    printf("\nEntered matrix:\n");
    for (i = 0; i < r2; i++) {
        for (j = 0; j < c2; j++) printf("%g   ", arr2[i][j]);
        printf("\n");
    }

    //Mutiplication
    float arr3[r1][c2];
    for (i = 0; i < r1; i++) {
        for (j = 0; j < c2; j++) {
            arr3[i][j] = 0;
            for (k = 0; k < c1; k++) arr3[i][j] += arr1[i][k] * arr2[k][j];
        }
    }

    printf("\nMultiplied matrix:\n");
    for (i = 0; i < r1; i++) {
        for (j = 0; j < c2; j++) printf("%g\t", arr3[i][j]);
        printf("\n");
    }
    return 0;
}