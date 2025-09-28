/*This program uses a function CornerSum which takes as a parameter, no. of rows and no. of 
columns of a matrix and returns the sum of the elements in the four corners of the 
matrix. The main function is used to test the function.*/

#include <stdio.h>
int row, col;
float CornerSum(float arr[row][col]){
    if (row == 1 && col == 1) return arr[0][0];
    else return arr[0][0] + arr[row - 1][0] + arr[0][col - 1] + arr[row - 1][col - 1];
}

int main(){
    printf("Enter number of rows and columns of your matrix --> ");
    scanf("%d %d", &row, &col);
    float matrix[row][col];
    printf("\nEnter %d elements of your matrix, one iņ each line below:\n", row * col);
    for (int i = 0; i < row; i++) for (int j = 0; j < col; j++) scanf("%f", &matrix[i][j]);
    float sum = CornerSum(matrix);
    printf("\nThe sum of the corner elements of the given matrix = %g", sum);
}