#include <stdio.h>

// Function to calculate Fibonacci sequence up to n terms
void fibonacci(int n) {
     long long first = 0, second = 1, next;
    printf("Fibonacci sequence up to %d terms:\n", n);
    for (int i = 1; i <= n; i++) {
        if (i == 1) {
            printf("%lld ", first);
            continue;
        }
        if (i == 2) {
            printf("%lld ", second);
            continue;
        }
        next = first + second;
        first = second;
        second = next;
        printf("%lld ", next);
    }
    printf("\n");
}

// Main function
int main() {
    int n;
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    fibonacci(n);
    return 0;
}

