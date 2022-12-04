#include <stdio.h>
#include <stdlib.h>

void part_1() {
    FILE *file = fopen("input_2_2022.txt", "r");
    size_t len = 10;
    char *line = malloc(len);
    int read;
    int ans = 0;
    while ((read = getline(&line, &len, file)) != -1) {
        if (line[0] == '\n') continue;
        int a = line[0], b = line[2];
        ans += b - 'X' + 1;
        int delta = b - a - 'X' + 'A';        
        if (delta == 0) {
            ans += 3;
        }
        else if (delta == -2 || delta == 1) {
            ans += 6;
        }
    }

    printf("%d\n", ans);
    fclose(file);
}

void part_2() {
    FILE *file = fopen("input_2_2022.txt", "r");
    size_t len = 10;
    char *line = malloc(len);
    int read;
    int ans = 0;
    while ((read = getline(&line, &len, file)) != -1) {
        if (line[0] == '\n') continue;
        int a = line[0], b = line[2];
        if (b == 'Z') {
            ans += 6;
            ans += (a - 'A' + 1) % 3 + 1; 
        }
        else if (b == 'X') {
            int res = (a - 'A');
            if (res == 0) res = 3;
            ans += res;
        }
        else {
            ans += 3;
            ans += a - 'A' + 1;
        }
    }
    printf("%d\n", ans);
    fclose(file);
}

int main() {
    part_1();
    part_2();
    return EXIT_SUCCESS;
}