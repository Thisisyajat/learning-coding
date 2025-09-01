#include <stdio.h>

int main(){
    float arr[20];
    int n;
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
    printf("]");
    return 0;
}