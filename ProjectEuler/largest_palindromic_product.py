"""Problem: Find the largest palindrome made from the product of two n-digit numbers.

How to take odd-length palindromes into account efficiently? They're not divisible by 11!

ANSWER: The largest product of any two 2-digit numbers will always have an even number of digits.
(Unless we are REALLY unlucky, and the largest palindrome is actually odd-length!)

Created By: AJ Singh
Date: April 13, 2021
Time: 9:30 PM MST
Time Taken:

Here are my problem-solving thoughts, and explanations of each solution I constructed. I did some rough work on paper
before I started coding, and am sharing what I did here.

    +++++ General Ideas/First Thoughts +++++

    +++++ Approach #1: Mathematical Approach +++++

    +++++ Approach #2: Iterative Approach +++++

    +++++ Analysis & Optimizations +++++

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def largest_palindromic_product(d):

    n = int("9" * d)
    largest = (0, 0, 0)
    while True:

        for i in range(n, 0, -1):

            if i % 11 != 0:
                continue

            for j in range(n, 10 ** (d - 1), -1):
                if i * j > largest[-1] and is_palindrome(i * j):
                    largest = (i, j, i * j)

        return largest


if __name__ == "__main__":
    x = 5
    print(largest_palindromic_product(x))
