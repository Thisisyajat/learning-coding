/*Binary search with in-buit sorting*/

#include <stdio.h>

int main(){
    int a[20], n, i = 0, swapped, temp, key;
    printf("Enter number of elements (<=20) --> ");
    scanf("%d", &n);
    printf("Enter the elements of the array in each line below:\n");
    while (i < n)
    {
        scanf("%d", &a[i]);
        i++;
    }
    printf("Entered array : [%d", a[0]);
    for (i = 1; i < n; i++)
    {
        printf(", %d", a[i]);
    }
    printf("]\n");
    /*Sorting array in ascending order, using bubble sort*/
    for (int pass = 0; pass < n - 1; pass++)
    {
        swapped = 0;
        for (i = 0; i < n - 1 - pass; i++)
        {
            if (a[i] > a[i+1])
            {
                temp = a[i];
                a[i] = a[i+1];
                a[i+1] = temp;
                swapped = 1;
            }          
        }
        if (!swapped) break;
    }
    printf("Ascending order array : [%d", a[0]);
    for (int i = 1; i < n; i++) {
        printf(", %d", a[i]);
    }
    printf("]\n");
    /*Searching using binary search*/
    printf("Enter element value to search --> ");
    scanf("%d", &key);
    int low = 0, high = n - 1, mid;
    do {
        mid = (low + high) / 2;
        if (key < a[mid]) high = mid - 1;
        else if (key > a[mid]) low = mid + 1;        
    } while (key != a[mid] && low <= high);
    if (key == a[mid]) printf("\n'%d' found in the array.",key);
    else printf("\n'%d' not found in the array.", key);
    return 0;
}