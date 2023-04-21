#include<iostream>
using namespace std;
void swap(int* a,int* b)
{
    int temp=*a;
    *a=*b;
    *b=temp;
}
namespace N
{
    void swapoon(int* a,int* b)
{
    int temp=*a;
    *a=*b;
    *b=temp;
}
}
void bubbleSort(int *a, int n)
{
	int i, j;
	for (i = 0; i < n - 1; i++)
		for (j = 0; j < n - i - 1; j++)
			if (a[j] > a[j + 1])
				swap(&a[j], &a[j + 1]);
}
void printArray(int *a, int n)
{
	int i;
	for (i = 0; i < n; i++)
		cout << a[i] << "  ";
}
void insertion_sort(int *a,int n)
{
    int j;
    int x;
    for(int i=1;i<n;i++)
    {
        j=i-1;
        x=a[i];
        while(j>=0 && a[j]>x)
        {
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=x;
    }
}
void merge(int *a,int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = a[l + i];
    for (j = 0; j < n2; j++)
        R[j] = a[m + 1 + j];
  
    i = 0; 
    j = 0; 
    k = l; 

    while (i < n1 && j < n2) 
    {
        if (L[i] <= R[j]) 
        {
            a[k] = L[i];
            i++;
        }
        else 
        {
            a[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) 
    {
        a[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) 
    {
        a[k] = R[j];
        j++;
        k++;
    }
}
void mergeSort(int *a, int l, int h)
{
	if (l >= h)
		return;

	int mid = l + (h - l) / 2;
	mergeSort(a, l, mid);
	mergeSort(a, mid + 1, h);
	merge(a, l, mid, h);
}
int partition(int *a,int l,int h)
{
    int pivot=a[l];
    int i=l;
    int j=h;
    while(i<j)
    {
        do
        {
            i++;
        }while(a[i]<=pivot);
        do
        {
            j--;
        } while (a[j]>=pivot);
        if(i<j)
        {
            swap(&a[i],&a[j]);
        }
    }
    swap(&pivot,&a[j]);
    return j;
}
void quick_sort(int *a,int l,int h)
{
    if(l<h)
    {
        int j;
        j=partition(a,l,h);
        quick_sort(a,l,j-1);
        quick_sort(a,j+1,h);
    }
}
void selectionSort(int *a, int n)
{
	int i, j, min;
	for (i = 0; i < n-1; i++)
	{
		min = i;
		for (j = i+1; j < n; j++)
		{
		if (a[j] < a[min])
			min = j;
		}
	    swap(&a[min], &a[i]);
	}
}
int binary_search(int *a,int l,int h,int k)
{
    int mid=l+(h-l)/2;
    if(l<=h)
    {
        if(a[mid]==k)
        {
            return mid;
        }
        else if(a[mid]<k)
        {
            return binary_search(a,mid+1,h,k);
        }
        else if(a[mid]>k)
        {
            return binary_search(a,l,mid-1,k);
        }
    }
    return -1;
}