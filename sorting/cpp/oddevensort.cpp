#include <bits/stdc++.h>
using namespace std;

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void oddEvenSort(int arr[], int n)
{
    bool sorted = false;
    while(!sorted) {
        sorted = true;
        for(int i = 1; i < n-1; i++){
            if(arr[i] > arr[i+1]) {
                swap(&arr[i], &arr[i+1]);
                sorted = false;
            }
        }
        for(int i = 0; i < n-1; i++){
            if(arr[i] > arr[i+1]) {
                swap(&arr[i], &arr[i+1]);
                sorted = false;
            }
        }
    }
}

/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
        cin>>arr[i];
    oddEvenSort(arr, n);
    printf("Sorted array: \n");
    printArray(arr, n);
    return 0;
}