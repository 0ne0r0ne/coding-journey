#include <stdio.h>

int main(void)
{
    //A program that input a 4-digit number from the user and sum its digits.    
    printf("Enter a 4-digit number.: ");
    
    int sayi1;
    
    scanf("%d", &sayi1);
    
    int bas_1, bas_2, bas_3, bas_4;
    
    bas_1 = sayi1 % 10;
    bas_2 = ((sayi1 % 100) - bas_1) / 10;
    bas_3 = ((sayi1 % 1000) - bas_1 - (bas_2*10)) / 100;
    bas_4 = (sayi1 - bas_1 - (bas_2*10) - (bas_3*100)) / 1000;
    
    
    printf("Here is sum of your integer: %d\n", bas_1 + bas_2 + bas_3 + bas_4);
    
    
    
    printf("\n");
    
    return 0;
  
}
