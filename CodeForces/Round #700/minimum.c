#include<stdio.h>
#include<stdlib.h>

#define not !
#define and &&
#define false 0
#define true 1

int request_value(int, int);

int main(void){
    int n;
    scanf("%d", &n);
    int left_range = 1, right_range = n;
    int *array = (int*)calloc((n+2), sizeof(int));
    array[0] = array[n+1] = n + 1;
 
    while(left_range < right_range){
        int middle = (int) ((right_range+left_range) / 2);
        if(request_value(middle, n))
            scanf("%d", &array[middle]);
        if(request_value(middle+1, n))
            scanf("%d", &array[middle+1]);
        if(array[middle] < array[middle+1])
            right_range = middle;
        else
            left_range = middle+1;
    }

    printf("! %d\n", left_range);
    fflush(stdout);
    free(array);
    return 0;
}

int request_value(int index, int n){
    if(index >= 1 and index <= n){
        printf("? %d\n", index);
        fflush(stdout);
        return true;
    }
}