// Implementation of selection sort in js
// Based on "sorting/python/selectionsort.py"

function selectionSort(numbers) {
    // Traverse through all array elements
    for (let i = 0; i < numbers.length; i++) {
        let minimumIndex = i;
        // Find the minimum element in remaining unsorted array
        for (let j = i + 1; j < numbers.length; j++) {
            if (numbers[minimumIndex] > numbers[j]) {
                minimumIndex = j;
            }
        }
        // Swap the minimum element with current index
        swapValues(numbers, minimumIndex, i);
    }
}

function swapValues(array, i, j) {
    const firstValue = array[i];
    array[i] = array[j];
    array[j] = firstValue;
}

// Test case
const numbers = [4877, 5280, 9977, 2105, 816, 7430, 8524, 4212, 8371, 8177];
console.log(numbers);
selectionSort(numbers);
console.log(numbers);
