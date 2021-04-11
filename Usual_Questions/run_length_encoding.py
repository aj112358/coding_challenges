"""Problem: Given a string, perform run-length-encoding on it, but only to a max of 9 elements!

Created By: AJ Singh
Date: April 7, 2021
Time: 5:00 PM MST
Time Taken: 25 minutes

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

import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        data = "AAAABBBCCDD"
        result = run_length_encoding(data)
        expected = "4A3B2C2D"
        self.assertEqual(result, expected)

    def test_case_2(self):
        data = "AAAAAAAAAAAAABBCCCCDD"
        result = run_length_encoding(data)
        expected = "9A4A2B4C2D"
        self.assertEqual(result, expected)

    def test_case_3(self):
        data = "aA"
        result = run_length_encoding(data)
        expected = "1a1A"
        self.assertEqual(result, expected)

    def test_case_4(self):
        data = "122333"
        result = run_length_encoding(data)
        expected = "112233"
        self.assertEqual(result, expected)

    def test_case_5(self):
        data = "************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"
        result = run_length_encoding(data)
        expected = "9*3*7^6$7%6!9A9A2A"
        self.assertEqual(result, expected)

    def test_case_6(self):
        data = ""
        result = run_length_encoding(data)
        expected = ""
        self.assertEqual(result, expected)


def run_length_encoding(string):

    if len(string) == 0:
        return ""

    i = 1
    encodings = list()
    current = string[0]
    num = 1
    while i < len(string):

        if num < 9 and string[i] == current:
            num += 1
        else:
            encodings.append(f"{num}{current}")
            num = 1
            current = string[i]
        i += 1

    encodings.append(f"{num}{current}")
    return "".join(encodings)


if __name__ == "__main__":

    x = "AAAABBBCCDD"
    print(run_length_encoding(x))

    unittest.main()
