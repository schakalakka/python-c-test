//
// Created by andreas on 3/29/16.
//

#include "fib.h"


int fib_rec(int n){
    if (n == 0) {
        return 0;
    }
    else if (n == 1) {
        return 1;
    }
    else {
        return fib_rec(n-1) + fib_rec(n-2);
    }
}

int fib_it(unsigned long int n){
    unsigned long int first = 0;
    unsigned long int second = 1;
    unsigned long int temp;
    if (n == 0){
        return 0;
    }
    else {
        for (int i = 0; i < n-1; i++){
            temp = first;
            first = second;
            second  = temp + second;
        }
    }
    return second;
}

int main(int argc, char *argv[]){
    if (argc != 2) {
        printf("Not enough parameters. cythontest n");
        exit(1);
    }

    int foo = atoi(argv[1]);

    //printf("\n%i\n", fib_rec(foo));
    printf("\n%lu\n", fib_it(foo));
}