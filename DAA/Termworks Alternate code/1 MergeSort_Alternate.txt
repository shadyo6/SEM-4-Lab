#include <stdio.h>
#include <stdlib.h>
#include<time.h>
#define MAX 10000

int *arr, *aux;

void merge(int,int,int);
void mergeSort(int,int);
void fillArray(int);
void showArray(int);

int main(void)
{
    int n,i,j;
    int low , high;
    clock_t s , e ;
    double  cpu_exe_t;
    printf("\nEnter the size of the array: ");
    scanf("%d",&n);

    arr = (int*)malloc(sizeof(int)*n);
    aux = (int*)malloc(sizeof(int)*n);

    low=0;
    high=n-1;

    fillArray(n);
    printf("\n\nUnsorted array");
    showArray(n);

    s=clock();
   // for(j=0;j<10000;j++)            //Delay loops
    for(i=0;i<10000;i++)
        mergeSort(low,high);
    e=clock();
    cpu_exe_t=(double)(e-s)/CLK_TCK;

    printf("\n\nSorted array");
    showArray(n);
    printf("\n\nCPU execution time is %lf\n\n",cpu_exe_t);
    return 0;
}

void fillArray(int n)
{
    int i;
    for(i=0;i<n;i++)
        *(arr+i)=rand()%100;
}

void showArray(int n)
{
    int i;
    printf("\nThe array elements are : \n\t");
    for(i=0;i<n;i++)
        printf("%d\t",*(arr+i));
}

void mergeSort(int low ,int high)
{
    int mid;

    if(low<high)
    {
        mid = (low+high)/2;
        mergeSort(low,mid);
        mergeSort(mid+1,high);
        merge(low,mid,high);
    }
}
void merge(int low ,int mid ,int high)
{
    int i=low , j=mid+1 , k=low;
    while(i<=mid && j<=high)
    {
        if(*(arr+i)<=*(arr+j))
        {
            *(aux+k)=*(arr+i);
            i++;
        }
        else
        {
            *(aux+k)=*(arr+j);
            j++;
        }
        k++;
    }
    while(i<=mid)
    {
        *(aux+k)=*(arr+i);
         k++;
         i++;
    }
    while(j<=high)
    {
        *(aux+k)=*(arr+j);
         k++;
         j++;
    }
    for(i=low ; i<=high ; i++)
        *(arr+i)=*(aux+i);
}
