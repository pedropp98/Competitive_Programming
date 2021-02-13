#include<stdio.h>

int main(void){
    int test_cases;
    scanf("%d", &test_cases);
    while(test_cases--){
        int x, y, qtd = 0;
        scanf("%d %d", &x, &y);    
        
        for(int a = x; a > 2; a--){
            for(int b = y; b > 1; b--){
                if((int)(a / b) == a % b)
                    qtd++;
            }
        }
        
        printf("%d\n", qtd);
        fflush(stdout);
    }
    return 0;
}