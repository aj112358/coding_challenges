"""Problem: Compute the minimum amount of *total* waiting time for all the input query times.

Created By: AJ Singh
Date: April 2, 2021
Time: 5:00 PM MT
Time Taken: 1hr 34mins

Here are my problem-solving thoughts, and explanations of each solution I constructed.

    +++++ General Ideas/First Thoughts +++++

- I felt a "greedy algorithm" was the way to go.
- To implement this, we need to start with the smallest time first, then move on to the next smallest time, and so on.
- To deal with this easily, we can simply sort the input list first.
- If the input array has length 0 or 1, the result is simply 0.
- If the input array has length 2, the result is simply the smaller of the two values.

    +++++ Approach #1: Brute-Force Algorithm +++++

- We can use nested loops.
- Outer loop -> iterates through entire array.
- Inner loop -> iterates through slices of the array (from 0 to outer loop index).
- The inner loop will compute the running-sum.

    +++++ Approach #2: Recursive Approach +++++

- We can compute the sum of the first n-1 elements in the array (n = length of array).
- We can recur on the sliced array where we disregard the last element.
- The base case is simply when the array has length 0 or 1 (no waiting time).

    +++++ Approach #3: Mathematical Approach +++++

- From my analysis, I discovered the following formula to solve this problem:
    - Denote: L = length of input list; q = input list

    # \sum_{i=0}^(L-2) ((L-1-i)* q[i])

- We can implement this formula easily in Python.

    +++++ Optimizations +++++

- I feel like the mathematical approach is the most optimal (but as a mathematician, I may be biased!).

- I feel like I *may* be able to determine a closed-form solution to the above summation, but due to the time
constraints of this assessment, I am not able to look into this right now.

- There may be a better/more efficient algorithm to apply than a "greedy algorithm", but I would have to do some more
research on that; otherwise, I feel my solution is a good start for now.

- For the first step (sorting), we can use any sorting algorithm (I would use either merge-sort or randomized quick-sort
for larger lists, or simply insertion sort for smaller lists).

- We may even be able to implement bucket-sort, if we know the range of input query times.

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""


def minimum_waiting_time(queries: list) -> int:
    """Computes the minimum total wait time for a list of queries.

    @param queries: Input list of execution times for each query.
    @return: Integer value of minimized total-wait-time.
    """

    queries.sort()  # Can use any sorting algorithm.

    # Dealing with some simple cases.
    if len(queries) in {0, 1}:
        return 0
    if len(queries) == 2:
        return min(queries)

    # ----- Brute-Force Approach ----- #

    # total_time = 0
    # for i in range(len(queries)-1):
    #     j = i
    #     while j >= 0:  # Iterating through sub-array queries[0:j].
    #         total_time += queries[j]
    #         j -= 1
    # return total_time

    # # Just trying to refactor the above code block.
    # total_time = 0
    # for i in range(len(queries)-1):
    #     for time in queries[:i+1]:
    #         total_time += time
    # return total_time

    # Just trying to refactor further.
    total_time = 0
    for i in range(len(queries)-1):
        total_time += sum(queries[:i+1])  # Python's built-in sum() function still iterates through entire input list.
    return total_time

    # ----- Recursive Approach ----- #

    # if len(queries) in {0, 1}:
    #     return 0
    # return sum(queries[:-1]) + minimum_waiting_time(queries[:-1])

    # ----- Mathematical Approach ----- #

    # total_time = 0
    # for i in range(len(queries)-1):
    #     total_time += (len(queries) - 1 - i) * queries[i]
    # return total_time


if __name__ == "__main__":

    x = [3, 2, 1, 2, 6]
    print("Minimum waiting time: ", minimum_waiting_time(x))
    # assert minimum_waiting_time(x) == 17, "WRONG!"

    x = [2, 1, 1, 1]
    print("Minimum waiting time: ", minimum_waiting_time(x))

    x = [3, 2]
    print("Minimum waiting time: ", minimum_waiting_time(x))

    x = [3]
    print("Minimum waiting time: ", minimum_waiting_time(x))

    x = []
    print("Minimum waiting time: ", minimum_waiting_time(x))
