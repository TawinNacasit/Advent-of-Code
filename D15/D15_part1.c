#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char str[100000];

int hash(char*val_as)
{
    int res=0;
    
    for (int i=0;val_as[i] != '\0';i++){
        res = ((((int)val_as[i])+res)*17)%256;
    }
    return res ;
}

int main()
{
    int reslut=0;
    int bufferLength = 100000;
    FILE *filePointer = fopen("text", "r");
    fgets(str, bufferLength, filePointer);
    fclose(filePointer);
    char *ch;
    ch = strtok(str, " ,");
    do
    {
        reslut += hash(ch);
        printf("%s\n", ch);
        ch = strtok(NULL, " ,");

    } while (ch != NULL);

    printf("%d",reslut);
}