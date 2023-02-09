from quicksort import quicksort
import unittest


# arr1 = [4, 3, 1]
# quicksort(arr1)
#
# print(arr1)


class TestQuicksort(unittest.TestCase):

    def test_small_array(self):
        arr1 = [4, 3, 1]
        quicksort(arr1)
        self.assertEqual(arr1, [1, 3, 4])

    def test_sorted_array(self):
        arr1 = [1, 3, 4]
        quicksort(arr1)
        self.assertEqual(arr1, [1, 3, 4])


if __name__ == '__main__':
    unittest.main()
