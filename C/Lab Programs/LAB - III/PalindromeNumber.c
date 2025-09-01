/*This program reverses the given number and checks if it is a palindrome or not.*/

#include <stdio.h>

int main(){
    int num, n, dig, rev = 0;
    printf("Enter a number --> ");
    scanf("%d", &num);
    n = num;
    while (num != 0){
        dig = num % 10;
        rev = rev * 10 + dig;
        num /= 10;
    }
    if (rev == n) printf("%d is a palindrome.\n",n);
    else printf("%d is not a palindrome.\n",n);
    return 0;
}
