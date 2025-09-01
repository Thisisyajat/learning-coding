// Program to find the largest and smallest number in the array.

#include <stdio.h>

int main(){
    float arr[20], max, min;
    int n;
    printf("Enter number of elements of the array --> ");
    scanf("%d", &n);
    printf("Enter elements of the array --> ");
    for (int i = 0; i < n; i++)
    {
        scanf("%f", &arr[i]);
    }
    printf("\n");
    max = min = arr[0];
    for (int i = 0; i < n; i++)
    {
        if (arr[i] > max) max = arr[i];
        else if (arr[i] < min) min = arr[i];
    }
    printf("Maximum value = %f\nMinimum value = %f", max, min);
    return 0;
}