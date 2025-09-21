#include<stdio.h>
int main(){
    float ans = 0, val;
    while (scanf("%[^'-1']", &val)) {
        ans += val;
        printf("%g", ans);
    } 
        
}