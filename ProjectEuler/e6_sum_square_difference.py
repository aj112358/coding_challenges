"""Problem:

Created By: AJ Singh
Date: April 13, 2021
Time: 12:20 AM MST
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


def sum_square_difference(n):

    return int((n*(n+1)/2)**2 - n*(n+1)*(2*n+1)/6)


if __name__ == "__main__":
    x = 10
    target = 2640
    result = sum_square_difference(x)
    assert result == target

    x = 100
    print(sum_square_difference(x))


