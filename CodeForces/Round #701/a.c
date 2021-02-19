#include<stdio.h>

// a = abs(a / b)
// b = b + 1

int main(void){
    int test_cases;
    scanf("%d", &test_cases);
    while(test_cases--){
        int a, b, a_copy, b_copy, resolution, answer;
        scanf("%d %d", &a, &b);
        if(a == 0){
            printf("0\n");
        }
        else{
            resolution = a + 3;
            for(int i = (b < 2) ? 2 - b : 0; i < resolution; i++){
                b_copy = b + i;
                a_copy = a;
                answer = i;
                while(a_copy){
                    a_copy /= b_copy;
                    answer++;
                }
                if(answer < resolution)
                    resolution = answer;
            }
            printf("%d\n", resolution);
        }
    }
    return 0;
}