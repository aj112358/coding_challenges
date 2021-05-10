"""Problem: Determine the largest product of 13 digits, in the 1000-digit number.

Created By: AJ Singh
Date: April 13, 2021
Time: 11:30 PM MST
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

import queue
from queue import Queue


def largest_product():

    with open("1000_digit_number.txt", mode="r") as file:

        q = Queue(maxsize=13)
        largest = 1

        # Initialize queue.
        for _ in range(13):
            digit = int(file.read(1))
            largest *= digit
            q.put(digit)

        while True:

            print(largest)

            removed_digit = q.get()
            digit = int(file.read(1))
            # if not digit:
            #     break
            q.put(digit)

            if digit == 0:

            current_product = largest
            if digit != 0:
                current_product = (largest / removed_digit) * digit

            if current_product > largest:
                largest = current_product

    return largest


if __name__ == "__main__":
    print(largest_product())
