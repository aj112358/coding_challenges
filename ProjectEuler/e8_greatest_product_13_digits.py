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

from queue import Queue


def reset_queue(q: Queue):
    while not q.empty():
        q.get()


def fill_queue(q: Queue, f_handle):
    largest = 1
    for _ in range(13):
        digit = int(f_handle.read(1))
        largest *= digit
        q.put(digit)
    return largest


def largest_product():

    with open("1000_digit_number.txt", mode="r") as file:

        q = Queue(maxsize=13)
        largest = 1

        # Initialize queue.
        new_largest = fill_queue(q, file)
        if new_largest > largest:
            largest = new_largest

        next_digit = file.read(1)
        while next_digit:

            next_digit = int(next_digit)
            if next_digit == 0:
                reset_queue(q)
                new_largest = fill_queue(q, file)
                if new_largest > largest:
                    largest = new_largest
            else:
                removed = q.get()
                new_largest = (new_largest / removed) * next_digit
                if new_largest > largest:
                    largest = new_largest

            next_digit = file.read(1)

    return largest


if __name__ == "__main__":
    print(largest_product())
    # with open("1000_digit_number.txt", mode="r") as file:
    #     x = file.read(1)
    #     while x:
    #         print(file.read(1))
    #         x = file.read(1)