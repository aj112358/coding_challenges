"""Problem: Determine the sum of all primes less than or equal to n.

Created By: AJ Singh
Date: April 13, 2021
Time: 7:55 PM MST
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


def sum_of_primes(n):

    primes = [2]
    test = 3
    while test <= n:

        if all(test % prime != 0 for prime in primes if prime < int(sqrt(test)) + 1):
            primes.append(test)
        test += 2

    return sum(primes)


if __name__ == "__main__":
    x = 10
    print(f"The sum of primes up to {x} is: {sum_of_primes(x)}")
