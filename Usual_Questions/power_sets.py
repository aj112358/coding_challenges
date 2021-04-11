"""Problem: Given a list of integers, return the power set.

Created By: AJ Singh
Date: April 4, 2021
Time: 4:15 PM MST
Time Taken:

Here are my problem-solving thoughts, and explanations of each solution I constructed. I did some rough work on paper
before I started coding, and am sharing what I did here.

    +++++ General Ideas/First Thoughts +++++

    +++++ Approach #1: Mathematical Approach +++++

    +++++ Approach #2: Recursive Approach +++++

    +++++ Analysis & Optimizations +++++

    +++++ Final Comments +++++

Thank you for taking the time to read this preamble, and for looking at my code below. I hope you and your team are
staying safe and healthy.

- AJ
"""

#
# class _Node:
#     """Class for node objects."""
#
#     __slots__ = "_element", "_parent", "_left", "_right"
#
#     def __init__(self, element, parent=None, left=None, right=None):
#         self._element = element
#         self._parent = parent
#         self._left = left
#         self._right = right


class Node:

    __slots__ = "data", "children"

    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


def create_tree(x, root):

    if len(x) == 0:
        return

    for elem in x:
        if elem > root.data:
            new_node = Node(elem)
            root.add_child(new_node)

            create_tree(x, new_node)

    return root

ps = []
new_set = []
def compute_power_set(node):

    if node is None:
        ps.append([])
        return

    if node.data != 0:
        new_set.append(node.data)

    for child in node.children:
        compute_power_set(child)
    # print(new_set)
    ps.append(new_set.copy())

    if len(new_set) != 0:
        new_set.pop()


    # return


    # if node.data == 0:
    #     ps.append([])

    # new_set.append(node.data)
    # ps.append(new_set)
    # print(ps)
    # for child in node.children:
    #     new_set.append(child.data)
    #     ps.append(new_set)
    #
    #     power_set(child, ps)

    #
    # # while node.children is not None:
    # new_set.append(node.data)
    # print("Children:", [child.data for child in node.children])
    # for child in node.children:
    #     # new_set.append(child.data)
    #     power_set(child, new_set)
    # ps.append(new_set)
    # # new_set.pop()
    # return ps


if __name__ == "__main__":

    my_list = [1,2,3,4]
    tree = create_tree(my_list, Node(0))
    # print(tree.data)
    result = compute_power_set(tree)
    # print(result)
    print(ps)


    # # print(tree.children)
    # for child in tree.children:
    #     print(child.data)
    #
    # for child in tree.children:
    #     for subchild in child.children:
    #         print(subchild.data)
    #
    # for child in tree.children:
    #     for subchild in child.children:
    #         for subsubchild in subchild.children:
    #             print(subsubchild.data)
    #
    # for child in tree.children:
    #     for subchild in child.children:
    #         for subsubchild in subchild.children:
    #             for subsubsubchild in subsubchild.children:
    #                 print(subsubsubchild.data)

    # for child in tree.children:
    #     for x in child.children:
    #         print(x.data)






######## OLD CODES #########

    # x.sort()  # We'll just assume it's sorted!

    # for elem in x:
    #     if elem > root.data:
    #         node = Node(elem)
    #         root.add_child(node)
    #
    # for child in root.children:
    #     for elem in x:
    #         if elem > child.data:
    #             node = Node(elem)
    #             child.add_child(node)