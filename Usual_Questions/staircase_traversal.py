"""Problem:

Created By: AJ Singh
Date: April 4, 2021
Time: 2:00 PM MST
Time Taken: ~2 hours

Here are my problem-solving thoughts, and explanations of each solution I constructed. I did some rough work on paper
before I started coding, and am sharing what I did here.

    +++++ General Ideas/First Thoughts +++++

- Upon drawing some pictures, I see we can use recursion (once we take any number of steps, the case of the remaining
steps is an easier case and was already dealt with).
- There is a Fibonacci-type pattern going on -> I can probably come up with some general math formula for this.
- So, we can probably use some kind of memoization technique (if we choose to use recursion).

    +++++ Approach #1: Mathematical Approach +++++

- I'm sure I can derive/construct a mathematical formula for any generic Fibonacci-type recursively-defined sequence,
but due to the time constraints, I cannot look into this right now (I'll be we can just Google such a formula too).

    +++++ Approach #2: Recursive Approach +++++

- Based on some examples I did, I found that we can describe this problem with the recursive relation:

n = 0, if h<0
n_0 = 1
n_1 = 1
n_h = \sum_{i=1}^m recursive(h-i)

- I implemented this approach in the code below.

    +++++ Analysis & Optimizations +++++

- For the recursive approach, we have time complexity O(m^h) (and I think the space complexity is O(h)?)
- I then refactored this a bit by using memoization, where we use a dictionary to keep track of already found data.
- This dictionary needs to be passed along with each recursive call.

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""


def traverse(height, max_steps, memo: dict ) -> int:

    # if height < 0:
    #     return 0
    # if height in {0, 1}:
    #     return 1
    #
    # num_ways = 0
    # for step_size in range(1, max_steps+1):
    #     num_ways += traverse(height-step_size, max_steps)
    #
    # return num_ways

    if height < 0:
        return 0

    if height in memo.keys():
        return memo[height]

    num_ways = 0
    for step_size in range(1, max_steps+1):
        num_ways += traverse(height-step_size, max_steps, memo)

    memo[height] = num_ways

    return num_ways


if __name__ == "__main__":

    h = 4
    steps = 3

    print(traverse(h, steps, {0: 1, 1: 1}))
