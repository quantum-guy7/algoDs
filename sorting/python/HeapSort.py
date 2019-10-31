class HeapSort:
    """
    This sorting algorithm segments the list into sorted and unsorted parts.
    It converts the unsorted segment of the list to a Heap data structure,
    so that we can efficiently determine the largest element.
    """

    def heapify(self, nums, heap_size, root_index):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child

        if largest != root_index:
            nums[root_index], nums[largest] = nums[largest], nums[root_index]
            self.heapify(nums, heap_size, largest)

    def heap_sort(self, nums):
        n = len(nums)
        for i in range(n, -1, -1):
            self.heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)

    def test_sorting(self):
        random_list_of_nums = [5, 2, 1, 8, 4]
        print(random_list_of_nums)
        self.heap_sort(random_list_of_nums)
        print(random_list_of_nums)


sorting_alg = HeapSort()
sorting_alg.test_sorting()
