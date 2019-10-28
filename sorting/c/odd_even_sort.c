#include<stdio.h>

#define SIZE 7

int main () {
  int i, flag, temp;
  int a[SIZE] = {1, 4, 5, 10, 2, 3, -1};
  
  do {
    flag = 0;
    //For Even Sort
    for (i = 0; i < SIZE - 1; i += 2) {
      //Swapping
      if (a[i] > a[i + 1]) {
	temp = a[i];
	a[i] = a[i + 1];
	a[i + 1] = temp;
	flag = 1;
      }
    }
    //For Odd Sort
    for (i = 1; i < SIZE - 1; i += 2) {
      //Swapping
      if (a[i] > a[i + 1]) {
	temp = a[i];
	a[i] = a[i + 1];
	a[i + 1] = temp;
	flag = 1;
      }
    }
  }
  while (flag);

  printf ("Array after Sorting\n");
  for (i = 0; i < SIZE; i++) {
    printf ("%d ", a[i]);
  }
  printf ("\n");
  return 0;
}
