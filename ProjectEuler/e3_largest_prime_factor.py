"""Problem: Determine the largest prime factor of 600851475143.

Created By: AJ Singh
Date: April 12, 2021
Time: 11:20 PM MST
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

from math import sqrt


def largest_prime_factor(n):
    """Return the largest prime factor of integer n."""

    if n < 2:
        raise ValueError("Input must be an integer greater than 1.")

    # primes = [2]
    # num = 3
    # while True:
    #
    #     while n % primes[-1] == 0:
    #         n = n // primes[-1]
    #
    #     if n == 1:
    #         return primes[-1]
    #
    #     if all(num % prime != 0 for prime in primes if prime < int(sqrt(num))+1):
    #         if n % num == 0:
    #             primes.append(num)
    #
    #     num += 2

    num = 2
    while n > 1:
        while n % num == 0:
            n = n // num
        num += 1
    return num-1


if __name__ == "__main__":

    # x = 600_851_475_143
    x = 21
    print(f"The largest prime factor of {x} is: {largest_prime_factor(x)}")
