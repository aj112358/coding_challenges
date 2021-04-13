"""Problem: Compute the 10,001 prime number.

Created By: AJ Singh
Date: April 12, 2021
Time: 10:40 PM MST
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


def compute_primes(n):
    """Computes the n-th prime number."""

    primes = [2]
    num = 3
    while len(primes) < n:

        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 1

    return primes[-1]


if __name__ == "__main__":

    x = 10001
    print(f"The {x}-th prime number is: {compute_primes(x)}")
