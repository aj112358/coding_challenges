"""Problem: Determine whether a target number is in a sorted array.

Created By: AJ Singh
Date: April 3, 2021
Time: 2:00 PM MST
Time Taken: 1 hour 14 minutes

Here are my problem-solving thoughts, and explanations of each solution I constructed.

    +++++ General Ideas/First Thoughts +++++

- Since the array is sorted, we can of course use a binary search.
- If the target is not in the given range (ie. is less than first, or greater than last element), can return -1
- If array has length 0, 1, 2, can do these cases more quickly
- Will need to use a pivot element to compare target with

    +++++ Approach #1: Brute-Force Algorithm +++++

- A simple solution is to just iterate through the array and manually look for the target element.
- Easy to implement with a loop.
- This doesn't use binary search though.

    +++++ Approach #2: Iterative Approach +++++

- In order to NOT slice the input array, we can use two pointers to keep track of the left and right indices.
- As we determine where the target is located relative to the pivot, we can update these pointers accordingly.
- We are done if we either find the target, or if the pointers cross each other.

    +++++ Approach #3: Recursive Approach +++++

- I know I can also implement the binary search in a recursive fashion.
- But due to the time constraint of this assessment, I'm not able to do so right now.

    +++++ Analysis & Optimizations +++++

- By using binary search (as in my iterative approach), the time complexity of my solution is O(log n).
- The space complexity is O(1).
- If we only need to know if the element *exists* in the array, I believe we can simply type-cast the array into a Python
set or dictionary, then can easily check if the target is contained.

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 5, 23, 111]
        target = 111
        expected = 3
        result = binary_search(array, target)
        self.assertEqual(result, expected)

    def test_case_2(self):
        array = [1, 5, 23, 111]
        target = 35
        expected = -1
        result = binary_search(array, target)
        self.assertEqual(result, expected)

    def test_case_3(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 1000
        expected = -1
        result = binary_search(array, target)
        self.assertEqual(result, expected)

    def test_case_4(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 61
        expected = 6
        result = binary_search(array, target)
        self.assertEqual(result, expected)

    def test_case_5(self):
        array = [1, 5]
        target = 5
        expected = 1
        result = binary_search(array, target)
        self.assertEqual(result, expected)

    def test_case_6(self):
        array = [1]
        target = 1
        expected = 0
        result = binary_search(array, target)
        self.assertEqual(result, expected)

    def test_case_7(self):
        array = []
        target = 1
        expected = -1
        result = binary_search(array, target)
        self.assertEqual(result, expected)


def binary_search(array, target):

    # ----- Brute-Force Approach ----- #

    # for index in range(len(array)):
    #     if array[index] == target:
    #         return index
    # return -1

    # ----- Iterative Approach ----- #

    left_pointer = 0
    right_pointer = len(array) - 1
    while left_pointer <= right_pointer:

        new_length = right_pointer - left_pointer + 1
        pivot = int(new_length/2) + left_pointer

        if array[pivot] == target:
            return pivot
        elif target > array[pivot]:
            left_pointer = pivot + 1
        else:
            right_pointer = pivot - 1
    else:
        return -1

    # ----- Recursive Approach ----- #
    # Due to time constraints, I'm not able to code this right now.


if __name__ == "__main__":

    # For manual testing.
    x = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    print(binary_search(x, target))

    # For automatic testing.
    unittest.main()
