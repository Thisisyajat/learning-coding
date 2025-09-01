#include <stdio.h>

int main(){
    float radius;
    printf("Enter radius of the sphere (cm) --> ");
    scanf("%f",&radius);
    printf("\nVolume of the sphere = %f",(4*3.1416*radius*radius*radius)/3);
    printf("\nSurface area of the sphere = %f",4*3.1416*radius*radius);
    return 0;
}
