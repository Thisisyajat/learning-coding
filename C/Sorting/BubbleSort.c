#include <stdio.h>
#include <stdlib.h>

int main(){
    int i, j, n, temp, swapped;
    char order;
    printf(("Enter number of elements --> "));
    if (scanf("%d", &n), n < 1){
        printf("Invalid number of elements.\nExiting...");
        exit(0);
    }
    int arr[n];
    printf("Enter the elements in each line below:\n");
    for (i = 0; i < n; i++) scanf("%d", &arr[i]);
    printf("Entered array: [%d", arr[0]);
    for (i = 1; i < n; i++) printf(", %d", arr[i]);
    printf("]\n");
    printf("Select order:\n\t1. Ascending order (type 'a')\n\t2. Descending order (type 'd')\nYour response --> ");
    scanf(" %c", &order);
    switch (order){
    case 'a':
        // Ascending order
        for (i = 0; i < n-1; i++) {
            swapped = 0;
            for (j = 0; j < n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    swapped = 1;
                }
            }
            if (!swapped) break;
        }
        break;
    case 'd':
        // Descending order
        for (i = 0; i < n-1; i++) {
            swapped = 0;
            for (j = 0; j < n-i-1; j++) {
                if (arr[j] < arr[j+1]) {
                    temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    swapped = 1;
                }
            } if (!swapped) break;
        }
        break;
    default:
        printf("Invalid option.\n");
        exit(1);
    }
    printf("Sorted array: [%d", arr[0]);
    for (i = 1; i < n; i++) printf(", %d", arr[i]);
    printf("]\n");
    return 0;
}