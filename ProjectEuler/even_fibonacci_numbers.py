"""Problem: Compute the sum of all the even Fibonacci numbers, up to a specified threshold (inclusive!).

Created By: AJ Singh
Date: April 4, 2021
Time: 7:20 PM MST
Time Taken: 1 hour 10 minutes (stupid geometric sequence mistake LOL)

Here are my problem-solving thoughts, and explanations of each solution I constructed. I did some rough work on paper
before I started coding, and am sharing what I did here.

    +++++ General Ideas/First Thoughts +++++

    +++++ Approach #1: Mathematical Approach +++++

    +++++ Approach #2: Iterative Approach +++++

    +++++ Analysis & Optimizations +++++

- phi^2 = phi + 1 can simplify the math formula!
- Time complexity = O(n), where n is number of Fib nums less/equal to threshold
- Indeed: n = floor(log(sqrt(5)*t + 0.5, base = phi)/3

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""

from math import sqrt, log, floor


def even_fibo_sum(t):

    # ----- Mathematical Approach ----- #

    # phi = (1+sqrt(5)) / 2
    # phi_bar = (1-sqrt(5)) / 2
    # n = floor(log(sqrt(5)*t+0.5, phi) / 3)
    #
    # # result = ((phi**(3*(n+1))-1)/(phi**3-1) - (phi_bar**(3*(n+1))-1)/(phi_bar**3-1)) / sqrt(5)
    # result = (((2*phi+1)**(n+1)-1)/(2*phi) - (phi_bar**(3*(n+1))-1)/(phi_bar**3-1)) / sqrt(5)
    # return result

    # ((2*phi+1)**(n+1)-1)/(2*phi)

    # ----- Iterative Approach ----- #

    # fib_nums = [0]
    #
    # a, b = 0, 1
    # while b <= t:
    #     fib_nums.append(b)
    #     a, b = b, a+b
    #
    # total = 0
    # for num in fib_nums:
    #     if num % 2 == 0:
    #         total += num
    # return total

    # Just trying to refactor the above code block.

    total = 0
    a, b = 0, 1

    while b <= t:  # I'm including the threshold if it's a Fibonacci number.
        a, b = b, a + b
        if a % 2 == 0:
            total += a

    return total


if __name__ == "__main__":

    print(int(even_fibo_sum(4000000)))
