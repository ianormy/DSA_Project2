"""
Union and Intersection

Your task for this problem is to fill out the union and intersection functions.

The union of two sets A and B is the set of elements which are in A, in B, or in both A and B.

The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members
of both the sets A and B.
"""
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = None
        while cur_head:
            if out_string:
                out_string += " -> " + str(cur_head.value)
            else:
                out_string = str(cur_head.value)
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    """The union of two sets A and B is the set of elements which are in A, in B, or in both A and B.

    Time Complexity: O(m+n).

    Here ‘m’ and ‘n’ are number of elements present in first and second lists respectively.
    First, traverse llist_1 and if it's unique add it to the output linked list - O(m)
    Second, traverse llist_2 and if it's unique and in the Hash-map from llist_1 add it to the output linked list - O(n)
    Hash-map lookup and addition takes O(1) time.

    Args:
        llist_1 (LinkedList): first linked list
        llist_2 (LinkedList): second linked list
    Returns:
         union of llist1 and llist2
    """
    unique_vals = set()
    union_llist = LinkedList()
    # traverse the first linked list
    if llist_1.head:
        node = llist_1.head
        while node:
            if node.value not in unique_vals:
                unique_vals.add(node.value)
                new_node = Node(node.value)
                union_llist.append(new_node)
            node = node.next
    # traverse the second linked list
    if llist_2.head:
        node = llist_2.head
        while node:
            if node.value not in unique_vals:
                unique_vals.add(node.value)
                new_node = Node(node.value)
                union_llist.append(new_node)
            node = node.next
    return union_llist if union_llist.head else None


def intersection(llist_1, llist_2):
    """The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members
    of both the sets A and B.

    Time Complexity: O(m+n).

    Here ‘m’ and ‘n’ are number of elements present in first and second lists respectively.
    First traverse llist-1, storing its elements in a Hash-map - O(m)
    Second, for every element in llist_2, check if it is already present in llist-1's Hash-map and
    hasn't already been added, then add it to the output linked list - O(n)
    Hash-map lookup and addition takes O(1) time.

    Args:
        llist_1 (LinkedList): first linked list
        llist_2 (LinkedList): second linked list
    Returns:
         intersection of llist1 and llist2
    """
    unique_vals_1 = set()  # handle non-unique values in first linked list
    unique_vals_out = set()  # handle non-unique values in second linked list
    intersection_llist = LinkedList()
    # traverse the first linked list getting the unique values
    if llist_1.head:
        node = llist_1.head
        while node:
            unique_vals_1.add(node.value)
            node = node.next
    # traverse the second linked list
    if llist_2.head:
        node = llist_2.head
        while node:
            if node.value in unique_vals_1 and node.value not in unique_vals_out:
                new_node = Node(node.value)
                intersection_llist.append(new_node)
                unique_vals_out.add(node.value)
            node = node.next
    return intersection_llist if intersection_llist.head else None




class UnionIntersectionTestCase(unittest.TestCase):
    def test_case_1(self):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()
        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
        element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        for i in element_1:
            linked_list_1.append(i)
        for i in element_2:
            linked_list_2.append(i)
        output_union = union(linked_list_1, linked_list_2)
        self.assertEqual('3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11', str(output_union))
        print(output_union)
        output_intersection = intersection(linked_list_1, linked_list_2)
        self.assertEqual('6 -> 4 -> 21', str(output_intersection))
        print(output_intersection)

    def test_case_2(self):
        linked_list_3 = LinkedList()
        linked_list_4 = LinkedList()
        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
        element_2 = [1, 7, 8, 9, 11, 21, 1]
        for i in element_1:
            linked_list_3.append(i)
        for i in element_2:
            linked_list_4.append(i)
        output_union = union(linked_list_3, linked_list_4)
        self.assertEqual('3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21', str(output_union))
        print(output_union)
        output_intersection = intersection(linked_list_3, linked_list_4)
        self.assertIsNone(output_intersection)


if __name__ == '__main__':
    unittest.main()
