//Program to insert an element to an array at a given position.

#include <stdio.h>

int main(){
    float arr[20], val;
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
    printf("Enter the position of element to insert and element value --> ");
    scanf("%d%f",&pos, &val);
    for (int i = n - 1; i >= pos - 1; i--)
    {
        arr[i+1] = arr[i];
    }
    arr[pos - 1] = val;
    printf("\nNew array:\n[%0.4f",arr[0]);
    for (int i = 1; i < (n + 1); i++)
    {
        printf(",  %0.4f", arr[i]);
    }
    printf("]");
    return 0;
}