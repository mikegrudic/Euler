#include "stdio.h"

int E(int x, int y){
    int count = 0;
    int temp;
    while (y!=0){
	temp = x;
	x = y;
	y = temp%y;
	count++;
    }
    return count;
}

int main(){
    int x,y;
    int sum = 0;
    for(x = 1; x <= 5000000; ++x){
	printf("%d\n",x);
	for (y = 1; y <= 5000000; ++y){
	    sum += E(x,y);
	}
    }
    return 0;
}
