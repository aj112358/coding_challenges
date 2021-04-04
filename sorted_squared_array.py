"""Problem: Compute the squares of all elements in an array, and return all in a new sorted array.

Created By: AJ Singh
Date: April 4, 2021
Time: 2:45 PM MST
Time Taken: ~40 minutes

Here are my problem-solving thoughts, and explanations of each solution I constructed. I did some rough work on paper,
and am sharing what I did here.

    +++++ General Ideas/First Thoughts +++++

- Since the array is sorted, I could probably use some type of binary search (ie. use pointers).
- Since negative integers are possible, we have to consider that the square of a negative integer could become bigger
than the square of a positive integer.
- Could just square all the numbers in one iteration, then sort afterwards.
- We don't need to worry about duplicate squares (since returned array must be same size of input array).

    +++++ Approach #1: Brute-Force Algorithm +++++

- We can iterate through array once and square each element, then simply use a sorting algorithm.

    +++++ Approach #2: Use a stack & two pointers +++++

- We can use a stack to store all the squared elements (have to push them onto the stack in descending order).
- Then, we simply pop from the stack into a new array to be returned.
- To find the largest element from input array (because squared negatives could become larger than squared positives),
we can use two pointers started from ends of the array moving inward.

    +++++ Analysis & Optimizations +++++

- I believe the stack/two-pointer approach is the more optimal.
- Time complexity for brute-force approach: O(n) + O(n*logn) -> O(n*logn).
- Time complexity for stack/two-pointer approach: O(n) + O(n) -> O(n) (iterate array once; remove all elements from stack).

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""

import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        array = [-5, -3, -1, 0, 2, 4, 6]
        expected = [0, 1, 4, 9, 16, 25, 36]
        result = sorted_squared(array)
        self.assertEqual(result, expected)

    def test_case_2(self):
        array = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        result = sorted_squared(array)
        self.assertEqual(result, expected)

    def test_case_3(self):
        array = [-5]
        expected = [25]
        result = sorted_squared(array)
        self.assertEqual(result, expected)

    def test_case_4(self):
        array = [-3, -2, -1, 0]
        expected = [0, 1, 4, 9]
        result = sorted_squared(array)
        self.assertEqual(result, expected)

    def test_case_5(self):
        array = [-1, -1, 2, 3, 3, 3, 4]
        expected = [1, 1, 4, 9, 9, 9, 16]
        result = sorted_squared(array)
        self.assertEqual(result, expected)


def sorted_squared(array: list) -> list:
    """Takes a sorted array of integers, and returns a new array of sorted squared integers.

    @param array: Sorted array to be squared.
    @return: Sorted array of squared elements.
    """

    # ----- Brute-Force Approach ----- #

    # return sorted([x**2 for x in array])

    # ----- Using Two Pointers and a Stack ----- #

    # stack = []
    #
    # left_pointer = 0
    # right_pointer = len(array)-1
    #
    # while left_pointer <= right_pointer:
    #
    #     if abs(array[right_pointer]) >= abs(array[left_pointer]):
    #
    #         stack.append(array[right_pointer]**2)
    #         right_pointer -= 1
    #     else:
    #         stack.append(array[left_pointer]**2)
    #         left_pointer += 1
    #
    # result = list()
    # while len(stack) > 0:
    #     result.append(stack.pop())
    #
    # return result

    # Just trying to refactor above code block.

    stack = []  # To store squared elements (in descending order).

    left_pointer = 0
    right_pointer = len(array)-1

    while left_pointer <= right_pointer:

        left = array[left_pointer]**2
        right = array[right_pointer]**2

        if right >= left:
            stack.append(right)
            right_pointer -= 1
        else:
            stack.append(left)
            left_pointer += 1

    result = list()  # List to re-order squared elements, to return.
    while len(stack) > 0:
        result.append(stack.pop())

    return result


if __name__ == "__main__":

    # For manual testing.
    x = [-5, -3, -1, 0, 2, 4, 6]
    print(*x, sep=" ")
    print(*sorted_squared(x), sep=" ")

    # For automated testing.
    unittest.main()
