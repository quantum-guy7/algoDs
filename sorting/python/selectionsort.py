# Implementation of Selection Sort 

def main():
    ''' Script entrypoint.'''
    numbers = [4877, 5280, 9977, 2105, 816, 7430, 8524, 4212, 8371, 8177]   
    print_numbers(numbers)
    selection_sort(numbers)
    print_numbers(numbers) 


def selection_sort(numbers: list):
    ''' Returns sorted list of numbers. '''

    # Traverse through all array elements 
    for i in range(len(numbers)):
        minimum_index = i

        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, len(numbers)):
            if numbers[minimum_index] > numbers[j]:
                minimum_index = j
        
        # Swap the minimum element with current index
        numbers[i], numbers[minimum_index] = numbers[minimum_index], numbers[i]

def print_numbers(numbers: list):
    ''' Print elements in a list seperated by comma.'''
    print(*numbers, sep = ", ")


main()
