#include<stdio.h>

int main()
{
    int arr[30];  
    int n,pos;    // n = number of elements; pos = holds index of minimum element
    int i,j,min;  //min = minimum element
    int temp;     // variable for swapping
    printf("\nNumber of elements :" );
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }


    for(i=0;i<n;i++)
    {
        pos=i;
        min=arr[i];
        for(j=i+1;j<n;j++)
        {
            if(arr[j]<min)
            {
                min=arr[j];
                pos=j;
            }
        }

        temp=arr[i];
        arr[i]=arr[pos];
        arr[pos]=temp;
    }



    for(i=0;i<n;i++)
    {
        printf("%d  ",arr[i]);
    }
}
