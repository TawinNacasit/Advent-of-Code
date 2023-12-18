#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char str[50000];
struct tuple *mapp[256][1000];
struct tuple
{
    char label[9];
    int focuslength;
};

int hash(char *val_as)
{
    int res = 0;

    for (int i = 0; val_as[i] != '\0'; i++)
    {
        res = ((((int)val_as[i]) + res) * 17) % 256;
    }
    return res;
}

int main()
{
    int c = 1;
    int result = 0;
    int bufferLength = 50000;
    FILE *filePointer = fopen("text", "r");
    fgets(str, bufferLength, filePointer);
    fclose(filePointer);
    char *ch;
    ch = strtok(str, " ,");

    int count[256];
    for (int i = 0; i < 256; i++)
    {
        count[i] = 0;
    }
    do
    {
        char label[9] = {0};
        char *opcode;

        int next = 0;
        int iasd = 0;
        for (; ch[iasd] != '\0' && ch[iasd] != '=' && ch[iasd] != '-' && iasd < 9; iasd++)
        {
            label[iasd] = ch[iasd];
        }
        opcode = &(ch[iasd]);
        int j = iasd + 1;
        for (; iasd < 9; iasd++)
        {
            label[iasd] = '\0';
        }
        switch (*opcode)
        {
        case '=':
        {
            int focalLength;
            int a = 0;
            focalLength = ch[j] - '0';
            for (int i = 0; i < count[hash(label)]; i++)
            {
                int dfgh = hash(label);
                struct tuple *dfh = mapp[hash(label)][i];
                if (strcmp(mapp[hash(label)][i]->label, label) == 0)
                {
                    mapp[hash(label)][i]->focuslength = focalLength;
                    a = 1;
                    break;
                }
            }
            if (a == 0)
            {
                struct tuple *tmp = (struct tuple *)(malloc(sizeof(struct tuple))); // dynamic
                strncpy(tmp->label, label, 9);
                tmp->focuslength = focalLength;

                mapp[hash(label)][count[hash(label)]] = tmp;
                count[hash(label)] = count[hash(label)] + 1;
            }

            break;
        }
        case '-':
        {
            int s = count[hash(label)];
            for (int i = 0; i < s; i++)
            {
                if (next == 1)
                {
                    mapp[hash(label)][i - 1] = mapp[hash(label)][i];
                }
                else if (strcmp(mapp[hash(label)][i]->label, label) == 0)
                {
                    mapp[hash(label)][i] = NULL;
                    next = 1;
                    count[hash(label)]--;
                }
            }
            break;
        }
        }
        ch = strtok(NULL, " ,");
        if (ch == NULL)
        {
            break;
        }

    } while (ch != NULL);
    for (int i = 0; i < 256; i++)
    {
        for (int l = 0; l < count[i]; l++)
        {
            result += (i + 1) * (l + 1) * mapp[i][l]->focuslength;
        }
    }
    printf("%d", result);
}