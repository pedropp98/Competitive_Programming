#include<stdio.h>
#include<stdlib.h>

#define BUFFER 4096
#define and &&

char *readline(FILE*);
char find_lowest(char);
char find_greatest(char);

int main(void){
    int test_cases;
    scanf("%d", &test_cases);
    getchar();
    while(test_cases--){
        char *string = readline(stdin);
        for(int i = 0; string[i] != 0; i++){
            if(i % 2 == 0){
                string[i] = find_lowest(string[i]);
            }
            else{
                string[i] = find_greatest(string[i]);
            }
        }
        printf("%s\n", string);
        free(string);
    }
    return 0;
}

char *readline(FILE *in){
    char *string = NULL;
    int pos = 0, character;
    do{
        if(pos % BUFFER == 0)
            string = (char*)realloc(string, (pos / BUFFER + 1) * BUFFER * sizeof(char));
        character = fgetc(in);
        if(character != 13)
            string[pos++] = character;
    }while(character != 10 and !feof(in));
    string[pos-1] = 0;
    string = (char*)realloc(string, pos * sizeof(char));
    return string;
}

char find_lowest(char character){
    if(character == 97)
        character += 1;
    else
        character = 97;
    return character;
}

char find_greatest(char character){
    if(character == 122)
        character -= 1;
    else
        character = 122;
    return character;
}