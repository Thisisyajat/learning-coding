#include <stdio.h>

int main(){
    float a = 30, b = 10, c = 5, d = 15;
    printf("Given values: a = 30, b = 10, c = 5, d = 15.\n\n");
    printf("(a + b) * c / d = %f", (a + b) * c / d);
    printf("\n((a + b) * c) / d  = %f", ((a + b) * c) / d);
    printf("\na + (b * c) / d = %f", a + (b * c) / d);
    printf("\n(a + b) * (c / d) = %f", ((a + b) * (c / d)));
    return 0;
}
