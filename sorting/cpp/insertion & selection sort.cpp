#include <iostream>
#include<vector>
using namespace std;

void selection(int *sel,int n)
{

	for (int i = 0; i < n; i++)
	{
		int min = 0;
		min = sel[i]; //selecting cureent unsorted element
		int j, k = 0;
		for (j = i; j < n; j++) 
		{
		//checking for all elements less or equal to current element
			if (sel[j] <= min)
			{
				min = sel[j]; //if yes, swapping the two elements
				k = j;
			}
    
		}
		
         // Swap the found minimum element with the first unsorted element
		int temp = 0;
		temp = min;
		min = sel[i];
		sel[i] = temp;
		sel[k] = min;


	}
	cout << "\n\nsorted order using SELECTION SORT\n";
	for (int p = 0; p < n; p++)
	{
		cout << sel[p] << " ";
	}
}
void insertion(int *arr,int n)
{
	int flag[10], index;
	for (int i = 0; i < n;i++)
	{
		flag[i] = 0;
	}
	flag[0] = 1;
	index = 0;
	
		
	int i=0,j=0,temp;
for(i=0;i<n;i++)
{
	temp=arr[i]; //selecting first unsorted index
	j=i-1; 
	/* Moving elements of arr[0..i-1], that are  
        greater than temp to one position ahead  
        of their current position */
	while((j>=0)&&(arr[j]>temp))
	{
		arr[j+1]=arr[j];
		j=j-1;
	}
	arr[j+1]=temp; //inserting the element at its sorted position
}	
    cout << "\n\nsorted order using INSERTION SORT\n";		  
	for (int i = 0; i < n; i++)
		cout << arr[i] << " ";
}
int main()
{
	vector<int> v;
	int ele = 0;
	cout << "enter the elements (enter 999 to end the stream of numbers):";
	int size = 0;
	for (int i = 0;; i++)
	{
		cin >> ele;
		{
			if (ele == 999)
				break;
		}
		v.push_back(ele);
		size += 1;
		
	}
	v.shrink_to_fit();
	int* arr = &v[0];
	//bubble(arr,size);
	selection(arr,size);
    cout<<"\n\n";
	insertion(arr, size);


	
}
/*

INPUT:"

4
5
2
99
56
0
23
999

OUTPUT:

enter the elements (enter 999 to end the stream of numbers):

sorted order using SELECTION SORT
0 2 4 5 23 56 99 



sorted order using INSERTION SORT
0 2 4 5 23 56 99 

*/