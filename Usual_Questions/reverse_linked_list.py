"""Problem: Given the head of a singly linked list, reverse the list in place.

Created By: AJ Singh
Date: April 7, 2021
Time: 3:10 PM MST
Time Taken: ~20 minutes (just to write code), then ~1 hour to get the unit tests working!

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


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(Node):  # To convert LL <-> arrays

    def array_to_list(self, values):
        current = self
        for value in values:
            current.next = Node(value)
            current = current.next
        return self


def list_to_array(node):
    values = []
    current = node
    while current is not None:
        values.append(current.value)
        current = current.next
    return values


class TestProgram(unittest.TestCase, LinkedList):

    def test_case_1(self):

        data = [0, 1, 2, 3, 4]
        test = LinkedList(data[0]).array_to_list(data[1:])  # This is now a legitimate LL.
        result = list_to_array(reverse_linked_list(test))  # My program to return the reversed LL.
        expected = data[::-1]
        self.assertEqual(result, expected)

    def test_case_2(self):

        data = [0, 1]
        test = LinkedList(data[0]).array_to_list(data[1:])  # This is now a legitimate LL.
        result = list_to_array(reverse_linked_list(test))  # My program to return the reversed LL.
        expected = data[::-1]
        self.assertEqual(result, expected)

    def test_case_3(self):

        data = [0]
        test = LinkedList(data[0]).array_to_list(data[1:])  # This is now a legitimate LL.
        result = list_to_array(reverse_linked_list(test))  # My program to return the reversed LL.
        expected = data[::-1]
        self.assertEqual(result, expected)


def reverse_linked_list(head: Node) -> Node:

    # Taking into account LLs with 0 or 1 nodes.
    if None in {head, head.next}:
        return head

    # There are at least two nodes.
    pointer1 = head
    pointer2 = pointer1.next
    pointer3 = pointer1.next.next

    head.next = None
    while pointer3 is not None:
        pointer2.next = pointer1  # Re-assign node's pointer to previous node.
        pointer1, pointer2, pointer3 = pointer2, pointer3, pointer3.next  # Shift all pointers forward through LL.

    pointer2.next = pointer1  # Re-assign tail node's pointer.

    return pointer2  # New head is tail of old LL.


if __name__ == "__main__":
    unittest.main()
