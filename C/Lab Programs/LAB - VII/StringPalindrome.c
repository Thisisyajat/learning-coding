#include <stdio.h>

int main()
{
    const int max = 100;
    char str[max], str2[max], temp;
    int i = 0, count = 0, palindrome = 1;
    printf("Enter your string below:\n");
    gets(str);
    // count characters
    while (str[i] != '\0')
        count++, i++;
    for (i = 0; i < count / 2; i++)
    {
        if (str[i] != str[count - i - 1])
        {
            palindrome = 0;
            break;
        }
    }
    if (palindrome) printf("\nIt is a palindrome.\nExiting...");
    else printf("\nIt is not a palindrome.\nExiting...");
    return 0;
}