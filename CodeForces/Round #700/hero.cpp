#include<stdio.h>
#include<stdlib.h>
#include<bits/stdc++.h>


void run();

int main(void){
    int test_cases;
    scanf("%d", &test_cases);
    while(test_cases--)
        run();
    return 0;
}

void run(){
    int A, B, n;
    int64_t damage = 0;
    scanf("%d %d %d", &A, &B, &n);
    
    int *a = (int*)malloc(n * sizeof(int));
    for(int i = 0; i < n; i++)
        scanf("%d", &a[i]);
    int *b = (int*)malloc(n * sizeof(int));
    for(int i = 0; i < n; i++)
        scanf("%d", &b[i]);
    for(int i = 0; i < n; i++)
        damage += int64_t(b[i] + A - 1) / A * a[i];
    for(int i = 0; i < n; i++){
        if(B - (damage - a[i]) > 0){
            printf("YES\n");
            free(a);
            free(b);
            return;
        }
    }
    printf("NO\n");

    free(a);
    free(b);
}