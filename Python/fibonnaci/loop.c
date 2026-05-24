#include <stdio.h>

int main() {
    int prev2 = 0, prev1 = 1;
    int newFibo;
    int loop;

    printf("Enter the number: ");
    scanf("%d", &loop);

    for(int fibo = 0; fibo < loop; fibo++){
        newFibo = prev1 + prev2;

        if (fibo % 2 == 0){
            printf("%d ", newFibo);
        }

        prev2 = prev1;
        prev1 = newFibo;
    }

    return 0;
}