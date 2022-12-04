#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file = fopen("input_4_2022.txt", "r");
    
    int t1, t2;
    t1 = t2 = 0;
    int size = 1000; // Number of lines in text file
    int overlap[size][2][2];

    size_t len = 20; // max len for a line
    char *line = malloc(len);
    int read;
    int current = 0;
    while ((read = getline(&line, &len, file)) != -1) {
        if (line[0] == '\n') continue;
        int i = -1;
        while (line[++i] != '\0') {
            if (line[i] == ',') {
                overlap[current][0][0] = t1;
                overlap[current][0][1] = t2;
                t1 = t2 = 0;
            }
            else if (line[i] == '\n') {
                overlap[current][1][0] = t1;
                overlap[current][1][1] = t2;
                t1 = t2 = 0;
            }
            else if (line[i] == '-') {
                t1 = t2;
                t2 = 0;
            }
            else {
                t2 = t2*10 + line[i] - '0';
            }
        }
        current++;
    }
    int ans = 0;
    int ans2 = 0;
    for (int i = 0; i < 1000; i++) {
        if ((overlap[i][0][0] <= overlap[i][1][0] && overlap[i][1][1] <= overlap[i][0][1]) 
            || (overlap[i][1][0] <= overlap[i][0][0] && overlap[i][0][1] <= overlap[i][1][1]) ) {
            ans++;
        }
        if (overlap[i][0][0] <= overlap[i][1][0] && overlap[i][1][0] <= overlap[i][0][1]
            || overlap[i][1][0] <= overlap[i][0][0] && overlap[i][0][0] <= overlap[i][1][1])
            ans2++;

    }
    printf("%d\n", ans);
    printf("%d\n", ans2);
}
