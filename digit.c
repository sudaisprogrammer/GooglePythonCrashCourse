#include<stdio.h>

void digit(int n){
    int count = 0;
    int num = n;
    while(num!=0){
        n = num%10;
        num = num/10;
        count++;
    }
    printf("digits are %d",count);
}

int main(){
    int num = -33772;
    digit(num);

    return 0;
}