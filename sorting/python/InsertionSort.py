class InsertionSort:
    """
    This algorithm segments the list into sorted and unsorted parts.
    It iterates over the unsorted segment,
    and inserts the element being viewed into the correct position of the sorted list.
    """

    @staticmethod
    def insertion_sort(nums):
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = item_to_insert

    def test_sorting(self):
        random_list_of_nums = [5, 2, 1, 8, 4]
        print(random_list_of_nums)
        self.insertion_sort(random_list_of_nums)
        print(random_list_of_nums)


sorting_alg = InsertionSort()
sorting_alg.test_sorting()

