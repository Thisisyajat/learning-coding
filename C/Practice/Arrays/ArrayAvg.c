/*This program computes the average of all elements in an array.*/

#include <stdio.h>
int main(){
    int a[20], n, i = 0;
    float avg;
    printf("Enter number of elements (<=20) --> ");
    scanf("%d", &n);
    printf("Enter the elements of the array in each line below:\n");
    while (i < n) {
        scanf("%d", &a[i]);
        i++;
    }
    printf("Entered array : [%d", a[0]);
    for (i = 1; i < n; i++) {
        printf(", %d", a[i]);
    }
    printf("]\n");
    for (i = 0; i < n; i++)
    {
        avg += a[i];
    }
    avg /= n;
    printf("The average of all elements in the array is %f.", avg);    
    return 0;
}
