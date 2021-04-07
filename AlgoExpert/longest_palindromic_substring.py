"""Problem: Given a string, return the longest palindromic substring.

Created By: AJ Singh
Date: April 7, 2021
Time: 1:20 PM MST
Time Taken: 1 hour 13 minutes

Here are my problem-solving thoughts, and explanations of each solution I constructed. I did some rough work on paper
before I started coding, and am sharing what I did here.

    +++++ General Ideas/First Thoughts +++++

- Would it matter if the substring has even or odd length?
- Can use two pointers, both will travel outwards
- Would need to check if there is the same element repeated multiple times at the "center" of a substring.
- So I can just use an iterative approach (this may be the brute-force/non-optimal solution though?).

    +++++ Assumptions +++++

- We will assume that substrings are *contiguous*.
- We will take any punctuation, spaces, etc *into account*.

    +++++ Approach #1: Iterative Approach +++++

- We only need to iterate through the entire string once.
- The two pointers will start at the same index.
- Then we will determine if there is a contiguous substring of all similar elements (if any)
- Then we will move the pointers simultaneously outwards
- Can stop (and hence go to next string element) if the pointers go out-of-index (ie. the entire string is a palindrome)
OR if two outer elements are non-equal.

    +++++ Approach #2: Recursive Approach +++++

    +++++ Analysis & Optimizations +++++

- The iterative approach has quadratic time complexity
- The space complexity is O(r), where r is the length of the current longest substring.
- I feel like there is a way to make this more optimal by taking into account the index in the string we are on, and
 the length of the current substring found so far.

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""

import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        x = "xyzzyx"
        expected = "xyzzyx"
        result = longest_palindrome(x)
        self.assertEqual(result, expected)

    def test_case_2(self):
        x = "axyzzyx"
        expected = "xyzzyx"
        result = longest_palindrome(x)
        self.assertEqual(result, expected)

    def test_case_3(self):
        x = "xyzzyxa"
        expected = "xyzzyx"
        result = longest_palindrome(x)
        self.assertEqual(result, expected)

    def test_case_4(self):
        x = "xyzazyx"
        expected = "xyzazyx"
        result = longest_palindrome(x)
        self.assertEqual(result, expected)

    def test_case_5(self):
        x = "xyz"
        expected = "x"
        result = longest_palindrome(x)
        self.assertEqual(result, expected)

    def test_case_6(self):
        x = "a"
        expected = "a"
        result = longest_palindrome(x)
        self.assertEqual(result, expected)

    def test_case_7(self):
        x = ""
        expected = ""
        result = longest_palindrome(x)
        self.assertEqual(result, expected)

    def test_case_8(self):
        x = "aaa"
        expected = "aaa"
        result = longest_palindrome(x)
        self.assertEqual(result, expected)


def longest_palindrome(string):

    if len(string) in {0, 1}:
        return string

    result = ""
    for index in range(len(string)):

        current_element = string[index]
        left_pointer = index
        right_pointer = index

        while right_pointer < len(string)-1:  # Check if there is a contiguous substring of all-equal elements.
            if string[right_pointer + 1] == current_element:
                right_pointer += 1
            else:
                break

        while left_pointer > 0 and right_pointer < len(string)-1:  # Check if you're strictly inside the string.
            if string[left_pointer-1] == string[right_pointer+1]:  # Move pointers outwards simultaneously.
                left_pointer -= 1
                right_pointer += 1
            else:
                break

        if len(string[left_pointer:right_pointer+1]) > len(result):
            result = string[left_pointer:right_pointer+1]

        if len(result) == len(string):
            break

    return result


if __name__ == "__main__":

    # For manual testing.
    x = "xyzzzyx"
    print(longest_palindrome(x))

    # For automatic testing.
    unittest.main()
