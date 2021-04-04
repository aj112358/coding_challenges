"""Problem: Compute the squares of all elements in an array, and return all in a new sorted array.

Created By: AJ Singh
Date: April 4, 2021
Time: 3:45 PM MST
Time Taken: ~58 minutes

Here are my problem-solving thoughts, and explanations of each solution I constructed. I did some rough work on paper
before I started coding, and am sharing what I did here.

    +++++ General Ideas/First Thoughts +++++

- Why are the teams in the 'competitions' array [home, away], but a 0/1 in the 'results' array represents away/home?????
- Maybe we need to determine how many teams there are first - it may help somehow?
- We can use a dictionary to keep track of each team's scores.
- The question only asks for which *team* wins, NOT the maximum score.

    +++++ Approach #1: Iterative (Brute-Force?) Algorithm +++++

- We will iterate both input arrays, determine which team won, and update the results in a dictionary.
- Then we can look through the dictionary of results for which team has the max score.

    +++++ Analysis & Optimizations +++++

- The initial iteration takes O(n) time complexity.
- To compute the winner, we use the max() function with the keyword parameter 'key=...' to compute.
- I'm not too sure how the max() function works under-the-hood in Python, but my guess is that it simply iterates
through the entire array to find the max. Hence, the time complexity would be O(n).
- BUT: I'm thinking the 'key=...' kwarg might impact this somehow.
- In our case, the 'key=...' is simply a way to retrieve a value for a given dictionary key, which I believe is done in
O(1) time.
- THUS: The overall time complexity is: O(n) + O(n)*O(1) -> O(n).

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""

import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        case = {
            "competitions": [
                ["HTML", "C#"],
                ["C#", "Python"],
                ["Python", "HTML"]
            ],
            "results": [0, 0, 1]
        }

        expected = "Python"
        actual = tournament_winner(case["competitions"], case["results"])
        self.assertEqual(actual, expected)

    def test_case_2(self):
        case = {
            "competitions": [
                ["HTML", "Java"],
                ["Java", "Python"],
                ["Python", "HTML"],
                ["C#", "Python"],
                ["Java", "C#"],
                ["C#", "HTML"]
            ],
            "results": [0, 1, 1, 1, 0, 1]
        }

        expected = "C#"
        actual = tournament_winner(case["competitions"], case["results"])
        self.assertEqual(actual, expected)

    def test_case_3(self):
        case = {
            "competitions": [
                ["HTML", "Java"],
                ["Java", "Python"],
                ["Python", "HTML"],
                ["C#", "Python"],
                ["Java", "C#"],
                ["C#", "HTML"],
                ["SQL", "C#"],
                ["HTML", "SQL"],
                ["SQL", "Python"],
                ["SQL", "Java"]
            ],
            "results": [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
        }

        expected = "C#"
        actual = tournament_winner(case["competitions"], case["results"])
        self.assertEqual(actual, expected)

    def test_case_4(self):
        case = {
            "competitions": [
                ["Bulls", "Eagles"]
            ],
            "results": [1]
        }

        expected = "Bulls"
        actual = tournament_winner(case["competitions"], case["results"])

        self.assertEqual(actual, expected)

    def test_case_5(self):
        case = {
            "competitions": [
                ["Bulls", "Eagles"],
                ["Bulls", "Bears"],
                ["Bulls", "Monkeys"],
                ["Eagles", "Bears"],
                ["Eagles", "Monkeys"],
                ["Bears", "Monkeys"]
            ],
            "results": [1, 1, 1, 1, 1, 1]
        }

        expected = "Bulls"
        actual = tournament_winner(case["competitions"], case["results"])
        self.assertEqual(actual, expected)


def tournament_winner(competitions, results):

    scores = dict()

    for i in range(len(results)):

        if results[i] == 0:
            scores[competitions[i][1]] = scores.get(competitions[i][1], 0) + 3
            scores[competitions[i][0]] = scores.get(competitions[i][0], 0) + 0
        else:
            scores[competitions[i][1]] = scores.get(competitions[i][1], 0) + 0
            scores[competitions[i][0]] = scores.get(competitions[i][0], 0) + 3

    # max_score = max(scores.values())
    max_team = max(scores, key=lambda k: scores[k])
    # print(max_team, max_score)

    return max_team


if __name__ == "__main__":

    # For manual testing.
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"] ]
    results = [0, 0, 1]
    tournament_winner(competitions, results)

    # For automated testing.
    unittest.main()
