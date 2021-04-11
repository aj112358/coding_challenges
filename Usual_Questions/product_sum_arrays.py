"""Problem:

Created By: AJ Singh
Date: April 7, 2021
Time: 5:50 PM MST
Time Taken:

Here are my problem-solving thoughts, and explanations of each solution I constructed. I did some rough work on paper
before I started coding, and am sharing what I did here.

    +++++ General Ideas/First Thoughts +++++

    +++++ Assumptions +++++

    +++++ Approach #1: Iterative Approach +++++

    +++++ Analysis & Optimizations +++++

- Time complexity = O(n)
- Space complexity = O(d)

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""


def product_sum(arr, depth=1):
    total = 0
    for elem in arr:
        if isinstance(elem, int):
            total += elem
        if isinstance(elem, list):
            total += product_sum(elem, depth+1)
    else:
        return depth*total


if __name__ == "__main__":

    my_array = [2, 4]
    print((product_sum(my_array)))

    my_array = [3, [2, [4, 5]], 1]
    print(product_sum(my_array))  # 62
