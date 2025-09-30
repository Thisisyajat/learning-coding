#include <stdio.h>
#include <stdlib.h>

int main(){
    int i, j, n, temp, pos;
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
        for (i = 0; i < n; i++) {
            pos = i;
            for (j = i + 1; j < n; j++) {
                if (arr[j] < arr[pos]) {
                    pos = j;
                }
            }
            temp = arr[i];
            arr[i] = arr[pos];
            arr[pos] = temp;
        }
        break;

    case 'd':
        // Descending order
        for (i = 0; i < n; i++) {
            pos = i;
            for (j = i + 1; j < n; j++) {
                if (arr[j] > arr[pos]) {
                    pos = j;
                }
            }
            temp = arr[i];
            arr[i] = arr[pos];
            arr[pos] = temp;
        }
        break;

    default:
        printf("Invalid response.\nExiting...");
        exit(0);
        break;
    }
/*     //Selection sort:
    for (i = 0; i < n; i++) {
        pos = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[pos]) {
                pos = j;
            }
        }
        temp = arr[i];
        arr[i] = arr[pos];
        arr[pos] = temp;
    } */
    printf("Sorted array: [%d", arr[0]);
    for (i = 1; i < n; i++) printf(", %d", arr[i]);
    printf("]\n");
    return 0;
}