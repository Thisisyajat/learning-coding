#include <stdio.h>
float addition();
float subtraction();
float multiplication();
float division();
void number();
void reset();
char mode;
float num,ans;
int count = 1;
int orig;

int main(){
    printf("Welcome to the calculator.\n");
    number();
    while (1){
        while ((getchar()) != '\n');
        printf("\nPlease select an operation:\n     - Addition (type 1)\n     - Subtraction (type 2)\n     - Multiplication (type 3)\n     - Division (type 4)\n     - Reset answer (type r)\n     - Exit (type e)\n\nYour response --> ");
        scanf("%c",&mode);
        if (mode == '1')
        {
            printf("\nAnswer --> %f\n", addition());
        }
        else if (mode == '2')
        {
            printf("\nAnswer --> %f\n", subtraction());
        }
        else if (mode == '3')
        {
            printf("\nAnswer --> %f\n", multiplication());
        }
        else if (mode == '4')
        {
            printf("\nAnswer --> %f\n", division());
        }
        else if (mode == 'r'){
            reset();
            printf("Reset successful.\n");
        }
        else if (mode == 'e')
        {
            printf("\nExiting...");
            break;
        }
        else printf("Invalid input. Try again.\n\n") ;
        }   
    return 0;
}

/* -----------------Number storage-----------------*/
void number(){
    orig = count;
    while (count > 10)
    {
        count -= 10;
    }
    switch (count)
    {
    case 1:
        printf("Enter %dst number --> ", orig);
        break;
    case 2:
        printf("Enter %dnd number --> ", orig);
        break;
    case 3:
        printf("Enter %drd number --> ", orig);
        break;
    default:
        printf("Enter %dth number --> ", orig);
        break;
    }
    scanf("%f",&ans);
    count = orig;
    count++;
}

/*------------------Reset function-----------------*/
void reset(){
    count = 1;
    num = 0;
}
/*--------------------Operations-------------------*/

float addition(){
    float a = num;
    number();
    return a + num;
}
float subtraction(){
    float a = num;
    number();
    return a - num;
}
float multiplication(){
    float a = num;
    number();
    return a * num;
}
float division(){
    float a = num;
    number();
    return a / num;
}
