import random


def quicksort_range(nums, fst, lst):
    if fst >= lst:
        return
 
    i, j = fst, lst
    pivot = nums[random.randint(fst, lst)]

    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

    quicksort_range(nums, fst, j)
    quicksort_range(nums, i, lst)


def quicksort(nums):
    return quicksort_range(nums, 0, len(nums) - 1)
