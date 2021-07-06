"""
Huffman Coding

There are two phases to Huffman encoding:

1. building the Huffman tree (a binary tree)
2. generating the encoded data

"""
import unittest
import heapq


class HuffmanNode:
    """The nodes that will be used to form the tree"""
    def __init__(self, value, key, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        self.key = key
        self.coding_val = ''  # will be either '0' or '1'

    def __lt__(self, other):
        """implementing this means that heapq will sort our values correctly"""
        return self.value < other.value

    def is_leaf_node(self):
        """is this a leaf node?

        Returns:
            True if this is a leaf node (i.e. no left or right nodes), otherwise False
        """
        return self.left is None and self.right is None


def generate_huffman_code_dict(huffman_code_dict, node, coding_val=''):
    """Recursive function to generate a dictionary of huffman codes from
    the leaf nodes of a huffman tree.

    Args:
        huffman_code_dict (dict): huffman code dictionary
        node (HuffmanNode): the current HuffmanNode we are processing.
        coding_val (str): the huffman code so far.
    """
    # huffman code for the current node - gets built as we traverse the tree
    huffman_code = coding_val + node.coding_val

    # if node is not a leaf node then traverse the left and right nodes
    if node.left:
        generate_huffman_code_dict(huffman_code_dict, node.left, huffman_code)
    if node.right:
        generate_huffman_code_dict(huffman_code_dict, node.right, huffman_code)

    # if node is a leaf node then add it to the dictionary
    if node.is_leaf_node():
        huffman_code_dict[node.key] = huffman_code


def create_huffman_tree(message):
    """Calculates a huffman tree for the input message

    Args:
        message (str): the message to create the huffman tree from
    Returns:
        root_node (HuffmanNode): root node of the huffman tree
    """
    if message is None:
        raise ValueError('message cannot be None')
    if len(message) == 0:
        raise ValueError('input message is empty')
    # determine the frequency of each character in the message
    char_freq = {}
    for c in message:
        char_freq[c] = char_freq.get(c, 0) + 1
    # put all of these in a min priority queue (this is the default type for the heapq module)
    h = []
    for k, v in char_freq.items():
        heapq.heappush(h, HuffmanNode(v, k))
    # now generate the huffman tree
    while len(h) > 1:
        left_node = heapq.heappop(h)
        right_node = heapq.heappop(h)
        val = left_node.value + right_node.value
        left_node.coding_val = '0'
        right_node.coding_val = '1'
        new_node = HuffmanNode(val, '#', left_node, right_node)  # signify it's a special node by using the '#' char
        heapq.heappush(h, new_node)
    root_node = heapq.heappop(h)
    # return the root node of the tree
    return root_node


class HuffmanCodingTestCase(unittest.TestCase):
    def test_valid_tree(self):
        huffman_tree = create_huffman_tree('AAAAAAABBBCCCCCCCDDEEEEEE')
        huffman_code_dict = {}
        generate_huffman_code_dict(huffman_code_dict, huffman_tree)
        self.assertEqual('000', huffman_code_dict['D'])
        self.assertEqual('001', huffman_code_dict['B'])
        self.assertEqual('01', huffman_code_dict['E'])
        self.assertEqual('10', huffman_code_dict['A'])
        self.assertEqual('11', huffman_code_dict['C'])

    def test_empty_message_raises_value_error(self):
        with self.assertRaises(ValueError):
            create_huffman_tree('')

    def test_none_message_raises_value_error(self):
        with self.assertRaises(ValueError):
            create_huffman_tree(None)


if __name__ == '__main__':
    unittest.main()
