"""Problem: Determine if a class photo is possible with given criteria.

Created By: AJ Singh
Date: April 3, 2021
Time: 4:30 PM MST
Time Taken: 56 minutes 29 seconds

Here are my problem-solving thoughts, and explanations of each solution I constructed.

    +++++ General Ideas/First Thoughts +++++

- If both input lists were sorted, then we could just compare the lists element-wise.
- If the minimum of one list is greater than the maximum of the other, then such a class photo *is* possible.

    +++++ Approach #1: Brute-Force Algorithm +++++

- We sort the lists first, then simply compare element-wise.

    +++++ Analysis & Optimizations +++++

- From sorting then iterating, the time complexity is: O(2*n*logn + n) -> O(n*logn).
- The space complexity is only O(1) (sorting is done in-place).
- If there is a way to avoid sorting, then perhaps we can improve the time complexity (perhaps a trade-off with space complexity?).

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        blue = [5, 8, 1, 3, 4]
        red = [6, 9, 2, 4, 5]
        result = class_photos(red, blue)
        expected = True
        self.assertEqual(result, expected)

    def test_case_2(self):
        blue = [6, 9, 2, 4, 5]
        red = [5, 8, 1, 3, 4]
        result = class_photos(red, blue)
        expected = True
        self.assertEqual(result, expected)

    def test_case_3(self):
        blue = [5, 8, 1, 3, 4, 9]
        red = [6, 9, 2, 4, 5, 1]
        result = class_photos(red, blue)
        expected = False
        self.assertEqual(result, expected)

    def test_case_4(self):
        blue = [5]
        red = [5]
        result = class_photos(red, blue)
        expected = False
        self.assertEqual(result, expected)

    def test_case_5(self):
        blue = [5, 2]
        red = [5, 1]
        result = class_photos(red, blue)
        expected = False
        self.assertEqual(result, expected)

    def test_case_6(self):
        blue = [1, 3, 4, 5, 8]
        red = [10, 11, 12, 13, 14]
        result = class_photos(red, blue)
        expected = True
        self.assertEqual(result, expected)


def class_photos(red, blue):

    red.sort()
    blue.sort()

    if red[0] > blue[-1] or blue[0] > red[-1]:
        return True

    # if red[0] == blue[0]:
    #     return False
    # elif red[0] > blue[0]:
    #     i = 1
    #     while i < len(red):
    #         if red[i] > blue[i]:
    #             i += 1
    #         else:
    #             return False
    # else:  # red[0] < blue[0]:
    #     i = 1
    #     while i < len(red):
    #         if red[i] < blue[i]:
    #             i += 1
    #         else:
    #             return False
    #
    # return True

    # ----- Trying to refactor the above code ----- #

    front_row = "Red" if red[0] < blue[0] else "Blue"
    for i in range(len(red)):
        if front_row == "Red":
            if red[i] >= blue[i]:
                return False
        else:
            if blue[i] >= red[i]:
                return False
    return True


if __name__ == "__main__":

    r = [5, 8, 1, 3, 4]
    b = [6, 9, 2, 4, 5]
    print(class_photos(r, b))

    unittest.main()
