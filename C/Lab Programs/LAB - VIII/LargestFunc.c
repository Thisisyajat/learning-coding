// This program uses a function Largest to find the maximum of a given list of numbers, and in a main program reads N numbers and find the largest among them using this function.
#include <stdio.h>

int n;
float Largest(float arr[]){
    int max = arr[0];
    for (int i = 1; i < n; i++) if (arr[i] > max) max = arr[i];
    return max;
}

int main(){
    printf("Enter number of elements --> ");
    scanf("%d", &n);
    float arr[n], max;
    printf("Enter %d elements below, one in each line:\n", n);
    for (int i = 0; i < n; i++) scanf("%f", &arr[i]);
    max = Largest(arr);
    printf("\nThe largest number entered = %g", max);
    return 0;
}