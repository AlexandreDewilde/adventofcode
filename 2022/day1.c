#include <stdio.h>
#include <stdlib.h>

void part_1() {
    FILE *file = fopen("input_1_2022.txt", "r");
    size_t len = 10;
    char *line = malloc(len);
    int read;
    int current_sum = 0;
    int ans = 0;
    while ((read = getline(&line, &len, file)) != -1) {
        if (line[0] == '\n') {
            if (ans < current_sum)
                ans = current_sum;
            current_sum = 0;
        }
        else {
            current_sum += atoi(line);
        }
    }

    printf("%d\n", ans);
    fclose(file);
}

void part_2() {
    FILE *file = fopen("input_1_2022.txt", "r");
    size_t len = 10;
    char *line = malloc(len);
    int read;
    int current_sum = 0;
    int a,b,c;
    a = b = c = 0;
    while ((read = getline(&line, &len, file)) != -1) {
        if (line[0] == '\n') {
            if (a <= current_sum) {
                c = b;
                b = a;
                a = current_sum;
            }
            else if (b <= current_sum) {
                c = b;
                b = current_sum;
            }
            else if (c < current_sum) {
                c = current_sum;
            }
            current_sum = 0;
        }
        else {
            current_sum += atoi(line);
        }
    }

    printf("%d\n", a + b + c);
    fclose(file);
}

int main() {
    part_1();
    part_2();
    return EXIT_SUCCESS;
}