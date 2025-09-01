//Program to delete an element in an array at a given position.

#include <stdio.h>

int main(){
    float arr[20];
    int n, pos;
    printf("Enter number of elements of the array --> ");
    scanf("%d", &n);
    printf("Enter elements of the array --> ");
    for (int i = 0; i < n; i++)
    {
        scanf("%f", &arr[i]);
    }
    printf("\n");
    printf("Array:\n[%0.4f",arr[0]);
    for (int i = 1; i < n; i++)
    {
        printf(",  %0.4f", arr[i]);
    }
    printf("]\n");
    printf("Enter the position of element to delete --> ");
    scanf("%d",&pos);
    if (pos < 1 || pos > n) {
        printf("Invalid position!\n");
        return 1;
    }
    for (int i = pos - 1; i < (n - 1); i++)
    {
        arr[i] = arr[i+1];
    }
    printf("\nNew array:\n[%0.4f",arr[0]);
    for (int i = 1; i < (n - 1); i++)
    {
        printf(",  %0.4f", arr[i]);
    }
    printf("]");
    return 0;
}