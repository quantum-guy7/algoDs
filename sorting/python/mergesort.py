def mergeSort(mylist, start, end):
    if end - start > 1:
        mid = (start + end) / 2 #cut the list into 2 equal parts
        mergeSort(mylist, start, mid) #recursivly sort first half of list
        mergeSort(mylist, mid, end) #recursivly sort second half of list
        merge(mylist, start, mid, end) #merge the newly osrted first and second half into one, sorted list
 
def merge(mylist, start, mid, end):
    left = mylist[start:mid] #first half sublist
    right = mylist[mid:end] #second half sublist
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end): #one-by-one ad the min element from both lists to the final list
        if (left[i] <= right[j]):
            mylist[k] = left[i]
            i = i + 1
        else:
            mylist[k] = right[j]
            j = j + 1
        k = k + 1

    # If the end of one of the lists is reached, simply 'dump' the rest of the sister list into the final list
    if start + i < mid: 
        while k < end:
            mylist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            mylist[k] = right[j]
            j = j + 1
            k = k + 1

mylist = [1,3,2,4,5,7,25] #Some example list
mergeSort(mylist, 0, len(mylist))