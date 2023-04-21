#include<iostream>
using namespace std;
#include"aiapexdev.h"
int main()
{
    int a[]={2,7,4,3,9,6,12,7699,45,23,87,54,67,43,17,65,34};
    int n=sizeof(a)/sizeof(a[1]);
    quick_sort(a,1,2);
    printArray(a,n);
    return 0;
}