#include <stdio.h>
void addition();

void main(){
    printf("Welcome to the calculator.\nAddition support only...\n");
    addition();
}

void addition(){
    int count = 0;
    float num1, num2, num, ans;
    int run = 1;
    while (run){
        count++;
        printf("Enter number %d --> ",count);
        scanf("%f",&num1);
        count++;
        printf("Enter number %d --> ",count);
        scanf("%f",&num2);
        ans = num1 + num2;
        printf("\nAnswer --> %f\n\nDo you want to add more numbers? 1 for yes, 0 for no --> ",ans);
        scanf("%d",&run);
        if (run == 1)
        {
            while (1)
            {
                count++;
                printf("Enter number %d --> ", count);
                scanf("%f",&num);
                ans += num;
                printf("\nAnswer --> %f\n\nDo you want to add more numbers? 1 for yes, 0 for no --> ",ans);
                scanf("%d",&run);
                if (run == 1)
                {
                    continue;
                }
                else printf("Okay, bye bye..."); break;
            }
            
        }
        else break;
    }    
}