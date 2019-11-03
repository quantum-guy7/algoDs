// Implementation of Bubble sort in JS
let bubbleSort = (arr, len) => {
    let swapped
    do {
        swapped = false
        for (let i = 0; i < len; i++) {
            if (arr[i] > arr[i + 1]) {
                let temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swapped = true
            }
        }
    } while (swapped)
    return arr
};

//Test case
let arr = [5,1,2,3,4]
console.log(bubbleSort(arr, arr.length))
