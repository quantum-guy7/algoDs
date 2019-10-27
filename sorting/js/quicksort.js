// Implementation of Quicksort in js
// Based on pseudo-algorithm from https://en.wikipedia.org/w/index.php?title=Quicksort&oldid=922709876#Lomuto_partition_scheme
function quickSort(array) {
    quickSortRec(array, 0, array.length - 1);
    return array;
}

function quickSortRec(array, lo, hi) {
    if (lo < hi) {
        const p = partition(array, lo, hi);
        quickSortRec(array, lo, p - 1);
        quickSortRec(array, p + 1, hi);
    }
}

function partition(array, lo, hi) {
    const pivot = array[hi];
    let i = lo;
    for (let j = lo; j < hi; j++) {
        if (array[j] < pivot) {
            swapValues(array, i, j);
            i++;
        }
    }
    swapValues(array, i, hi);
    return i;
}

function swapValues(array, i, j) {
    const firstValue = array[i];
    array[i] = array[j];
    array[j] = firstValue;
}

// Test case
const arrayToSort = [5, 1, 2, 3, 4, 10, 41, 32];
console.log(quickSort(arrayToSort));
