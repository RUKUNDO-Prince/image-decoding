#include <stdio.h>
#include <stdlib.h>

// Structure definition
struct Car {
    int numberOfDoors;
    int numberOfSits;
    char color[20];
};

int main() {
    struct Car* car1;
    struct Car* car2;

    // Dynamically allocate memory for car1
    car1 = (struct Car*)malloc(sizeof(struct Car));

    // Read values for car1 members from the user
    printf("Enter values for member elements of car1: \n");
    scanf("%d %d %s", &(car1->numberOfDoors), &(car1->numberOfSits), car1->color);

    // Dynamically allocate memory for car2
    car2 = (struct Car*)malloc(sizeof(struct Car));

    // Read values for car2 members from the user
    printf("Enter values for member elements of car2: \n");
    scanf("%d %d %s", &(car2->numberOfDoors), &(car2->numberOfSits), car2->color);

    // Print values for car1
    printf("Values you gave for car1:\n");
    printf("Doors: %d\n", car1->numberOfDoors);
    printf("Sits: %d\n", car1->numberOfSits);
    printf("Color: %s\n", car1->color);

    // Print values for car2
    printf("Values you gave for car2:\n");
    printf("Doors: %d\n", car2->numberOfDoors);
    printf("Sits: %d\n", car2->numberOfSits);
    printf("Color: %s\n", car2->color);

    // Free the allocated memory
    free(car1);
    free(car2);

    return 0;
}

