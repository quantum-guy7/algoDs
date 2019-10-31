'''
HEAP SORT
@autor CristopherA96
According to the theory:
Heap sort is a comparison based sorting technique 
based on Binary Heap data structure. It is similar
to selection sort where we first find the maximum
element and place the maximum element at the end. 
We repeat the same process for remaining element.
'''  
def heap(arr, n, i): 
    largest = i       # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heap(arr, n, largest) 

# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heap(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heap(arr, i, 0) 
  
# Testign the code 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("The sorted array is the next: ") 
for i in range(n): 
    print ("%d" %arr[i]), 