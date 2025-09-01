# include <stdio.h>

int main(){
    int n, k;
    printf("Enter number of tables to generate (starting from 1),\nand number of terms in each table --> ");
    scanf("%d%d", &n, &k);
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= k; j++){
            printf("%d   ", i * j);
        }
        printf("\n");
    }
    return 0;
}