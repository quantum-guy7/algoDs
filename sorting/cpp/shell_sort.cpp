#include <iostream>
using namespace std;

void shell_sort(int a[], int n) {
    int gap, i, j, temp;
    for (gap = n / 2; gap > 0; gap /= 2) {
        for (i = gap; i < n; i++) {
            temp = a[i];

            for (j = i; j >= gap && a[j - gap] > temp; j -= gap)
                a[j] = a[j - gap];

            a[j] = temp;
        }
    }
}

void printArray(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++) cout << arr[i] << " ";
    cout << endl;
}

int main() {
    int a[] = {3, 6, 1, 3, 8, 9, 5, 7};
    int n = sizeof(a) / sizeof(a[0]);
    shell_sort(a, n);

    printArray(a, n);
}