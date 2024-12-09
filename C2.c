#include <stdio.h>

void checkEvenOdd(int num) {
    if (num % 2 == 0) {
        printf("%d is an even number.\n", num);
    } else {
        printf("%d is an odd number.\n", num);
    }
}

int main() {
    int num;
    printf("Enter an integer to check if it's even or odd: ");
    scanf("%d", &num);
    checkEvenOdd(num);
    return 0;
}
