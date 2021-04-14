"""Problem: Determine the LCM of all numbers 1, 2, ... , n

Created By: AJ Singh
Date: April 13, 2021
Time: 7:40 PM MST
Time Taken: 10 minutes

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

from numpy import lcm


def lowest_common_multiple(n):

    result = lcm(1, 2)
    for num in range(3, n+1):
        result = lcm(result, num)
    return result


if __name__ == "__main__":

    x = 100
    print(f"LCM is: {lowest_common_multiple(x)}")
