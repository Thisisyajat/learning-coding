/*This program counts the number of prime numbers and composite numbers entered by user, and exits when -1 is entered.*/

#include <stdio.h>

int main(){
    int pcount = 0, ccount = 0, num, isPrime;
    do {
        printf("Enter a number (To exit program enter '-1') --> ");
        scanf("%d", &num);
        if (num != 1){
            if (num > 1){
                isPrime = 1;
                for (int i = 2; i <= num / 2; i++){
                    if (num % i == 0){
                        isPrime = 0;
                        break;
                    }
                }
                if (isPrime) pcount++;
                else ccount++;
            }
        }
        else continue;
    } while (num != -1);
    printf("\nNumber of prime numbers entered = %d\nNumber of composite numbers entered = %d\n",pcount,ccount);
    printf("Exiting...");
    return 0;
}
