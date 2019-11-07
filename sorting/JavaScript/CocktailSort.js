//Cocktail Sort works just like bubble sort, but it starts to sort the array from both sides
CocktailSort = (arr, n) => {
  var swap = true;
  var start = 0;
  var end = n - 1;
  while (swap) {
    swap = false;
    for (let i = start; i < end; i++) {
      if (arr[i] > arr[i + 1]) {
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        swap = true;
      }
    }
    if (!swap) break;
    swap = false;
    end--;
    for (let i = end - 1; i >= start; i--) {
      if (arr[i] > arr[i + 1]) {
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        swap = true;
      }
    }
    start++;
  }
};

//Test Case
const array = [9, 3, 6]; //Your array here
const n = array.length;
CocktailSort(array, n);
console.log("This is sorted array: " + array);
