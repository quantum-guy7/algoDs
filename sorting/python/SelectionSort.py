class SelectionSort:
    """
    This algorithm segments the list into two parts: sorted and unsorted.
    We continuously remove the smallest element of the unsorted segment of the list and append it to the sorted segment.
    """

    @staticmethod
    def selection_sort(nums):
        for i in range(len(nums)):
            lowest_value_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

    def test_sorting(self):
        random_list_of_nums = [5, 2, 1, 8, 4]
        print(random_list_of_nums)
        self.selection_sort(random_list_of_nums)
        print(random_list_of_nums)


sorting_alg = SelectionSort()
sorting_alg.test_sorting()

