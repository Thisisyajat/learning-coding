#include <stdio.h>

int main(){
    float arr[20], temp;
    int n, isSwap = 0, run = 1;
    char mode;
    printf("Enter number of elements of the array --> ");
    scanf("%d", &n);
    printf("Enter elements of the array --> ");
    for (int i = 0; i < n; i++)
    {
        scanf("%f", &arr[i]);
    }
    printf("\n");
    printf("Entered Array:\n[%f",arr[0]);
    for (int i = 1; i < n; i++)
    {

        printf(",  %f", arr[i]);
    }
    printf("]\n");
    while (run)
    {
        printf("\nSort by:\n\t1. Ascending order (type 'a')\n\t2. Descending order (type 'd')\nTo exit type any other char.\n\nYour response --> ");
        scanf(" %c", &mode);
        switch (mode)
        {
        case 'a':
            while (1)
            {
                isSwap = 0;
                for (int i = 0; i < n - 1; i++)
                {
                    if (arr[i] > arr[i + 1])
                    {
                        temp = arr[i];
                        arr[i] = arr[i+1];
                        arr[i+1] = temp;
                        isSwap = 1;
                    }
                }
                if (!isSwap) break;
            }
            printf("\nArray in ascending order:\n[%f",arr[0]);
            for (int i = 1; i < n; i++) printf(",  %f", arr[i]);
            printf("]\n\n");
            break;
        
            case 'd':
            while (1)
            {
                isSwap = 0;
                for (int i = 0; i < n - 1; i++)
                {
                    if (arr[i] < arr[i + 1])
                    {
                        temp = arr[i];
                        arr[i] = arr[i+1];
                        arr[i+1] = temp;
                        isSwap = 1;
                    }
                }
                if (!isSwap) break;
            }
            printf("\nArray in descending order:\n[%f",arr[0]);
            for (int i = 1; i < n; i++) printf(",  %f", arr[i]);
            printf("]\n\n");
            break;
        
        default:
            printf("\nExiting...");
            run = 0;
            break;
        }
    }
    return 0;
}