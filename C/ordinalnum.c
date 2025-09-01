/*Ordinal number program*/

#include <stdio.h>

int main(){
    int num, orig;
    printf("Enter a number --> ");
    scanf("%d",&num);
    orig = num;
    while (num > 10)
    {
        num -= 10;
    }
    switch (num)
    {
    case 1:
        printf("\n%dst", orig);
        break;
    case 2:
        printf("\n%dnd", orig);
        break;
    case 3:
        printf("\n%drd", orig);
        break;
    default:
        printf("\n%dth", orig);
        break;
    }
    return 0;
}