/** Selection sort program in c++ **/
#include<iostream>
#include<conio.h>
using namespace std;
//A class which is used to get the values
class data{
	protected:
		int i,j,n,a[100],l,ind;
		public:
			void get();
			void dis();
};
//A class which contain the function which does the selection sort
class selection:public data{
	public:
		void sort();
		void swap(int,int);
};
// To get values
void data::get(){
	cout<<"Enter the size"<<endl;
	cin>>n;
	cout<<"Enter the elements"<<endl;
	for(i=0;i<n;i++)
	{
		cin>>a[i];
	}
}
// To display the output
void data::dis(){
	cout<<"The sorted elements are ";
	for(i=0;i<n;i++)
	{
		cout<<a[i];
	}
}
// Selection sort
void selection::sort(){
	for(i=0;i<n-1;i++)
	{
		l = a[i];
		ind = i;
		for(j=i+1;j<n;j++)
		{
			if(a[l]>a[j])	
			{
				l = j;	
			}	
		}		
		swap(l,ind);
	}
}
// Swapping function
void selection::swap(int l,int id)
{
	int temp;
	temp = a[l];
	a[l] = a[ind];
	a[ind] = temp;
}
int main()
{
	selection s;
	s.get();
	s.sort();
	s.dis();	
	getch();
	return 0;
}