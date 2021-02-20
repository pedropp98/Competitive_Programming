#include<stdio.h>

int main(void){
    int floor = 0, first_basement = 0, position = 1;
    while(!feof(stdin)){
        int character = getchar();
        if(character == 40)
            floor++;
        else if(character == 41)
            floor--;
        if(floor < 0 && first_basement == 0)
            first_basement = 1;
        else if(first_basement == 0)
            position++;
    }
    printf("Part one: %d\n", floor);
    printf("Part two: %d\n", position);
    return 0;
}

