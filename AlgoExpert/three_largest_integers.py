"""Problem:

Created By: AJ Singh
Date: April 7, 2021
Time: 6:20 PM MST
Time Taken:

Here are my problem-solving thoughts, and explanations of each solution I constructed. I did some rough work on paper
before I started coding, and am sharing what I did here.

    +++++ General Ideas/First Thoughts +++++

    +++++ Assumptions +++++

    +++++ Approach #1: Iterative Approach +++++

    +++++ Analysis & Optimizations +++++

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""

import heapq


def top_nums(array, top=3):

    # ----- Brute-Force Solution ----- #

    # array.sort()
    # return array[len(array)-3:]

    # ----- Iterative Solution ----- #

    if len(array) == 3:
        return sorted(array)

    # third, second, first = sorted(array[:3])
    # for elem in array[3:]:
    #
    #     if elem >= first:
    #         third, second, first = second, first, elem
    #     elif elem >= second:
    #         third, second = second, elem
    #     elif elem > third:
    #         third = elem
    #
    # return [third, second, first]

    # ----- Trying to generalize above code to ANY k largest numbers ----- #

    # largest = [None] * top


    # ---- Can just use a heap? ----- #

    heap = []
    for item in array[:top]:
        heapq.heappush(heap, item)
    # print(heap)

    for item in array[top:]:
        if item > heap[0]:
            heapq.heappushpop(heap, item)
    # print(heap)

    return sorted(heap)



if __name__ == "__main__":

    x = [1, 200, 3, 4, 5, 200]
    print(x)
    print(top_nums(x))