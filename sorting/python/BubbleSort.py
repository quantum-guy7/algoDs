class BubbleSort:
    """
    This sorting algorithm iterates over a list,
    comparing elements in pairs and swapping them until the larger elements "bubble up" to the end of the list,
    and the smaller elements stay at the "bottom".
    """

    @staticmethod
    def bubble_sort(nums):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True

    def test_sorting(self):
        random_list_of_nums = [5, 2, 1, 8, 4]
        print(random_list_of_nums)
        self.bubble_sort(random_list_of_nums)
        print(random_list_of_nums)


sorting_alg = BubbleSort()
sorting_alg.test_sorting()
