#include <stdio.h>

int main() {
    int num;

    while (1) {
        printf("Enter a number (or 'exit' to exit): ");
        if (scanf("%d", &num) == 0) {
            // if input is not an integer, break out of the loop
            break;
        }
        if (num == 0) {
            printf("The number is zero\n");
        } else if (num > 0) {
            printf("The number is positive\n");
        } else {
            printf("The number is negative\n");
        }
    }

    printf("Exiting the program\n");

    return 0;
}

