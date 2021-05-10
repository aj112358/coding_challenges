"""Problem: Compute the sum of all the multiples of 3 and 5, up to a specified threshold.

Created By: AJ Singh
Date: April 4, 2021
Time: 6:00 PM MST
Time Taken: ~40 minutes

Here are my problem-solving thoughts, and explanations of each solution I constructed. I did some rough work on paper
before I started coding, and am sharing what I did here.

    +++++ General Ideas/First Thoughts +++++

- We have to take multiples of 15 into account (they are over counted, so we'll need to subtract).
- We can use an arithmetic sequence to get closed-form solutions for each individual summation.
- We'll need to figure out how many terms in each multiples sequence we should take.
- NEEDS TO BE STRICTLY LESS THAN THE THRESHOLD!

    +++++ Approach #1: Mathematical Approach +++++

- The formula for the sum of integers 1,...,n is: n(n+1)/2
- The *amount* of multiples we need is: \floor(threshold/multiple)
- Regarding the threshold, we have to use the value that is one less (because we want to compute *strictly* smaller).

    +++++ Approach #2: Iterative Approach +++++

- We can simply run through all the numbers less than the threshold, and check if they are multiples of 3 or 5.
- This actually avoids double-counting because of Python's short-circuiting ability!

    +++++ Analysis & Optimizations +++++

- For known inputs, the mathematical approach takes O(1) time.
- The iterative approach takes O(t) time.
- For future considerations, we can generalize our solution to any amount of input numbers.
- We can also think about how to take into account the case where the input numbers are *not* co-prime.
- Can probably use the LCM of the numbers somehow (pair-wise, triple-wise, etc).
- In these cases, we simply apply the "Principle of Inclusion-Exclusion".

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""

import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        threshold = 1000
        a, b = 3, 5
        expected = 233168
        actual = sum_multiples(a, b, threshold)
        self.assertEqual(actual, expected)


def sum_multiples(t, *args):
    """hello"""

    # ----- Iterative Approach ----- #

    total = 0
    for i in range(t):
        if any(i % x == 0 for x in args):
            total += i
    return total

    # ----- Mathematical Approach ----- #

    # return (a*int((t-1)/a)*(int((t-1)/a)+1) + b*int((t-1)/b)*(int((t-1)/b)+1) - (a*b)*int((t-1)/(a*b))*(int((t-1)/(a*b))+1)) // 2


if __name__ == "__main__":

    print(sum_multiples(20, 2, 3, 5))

    # unittest.main()
