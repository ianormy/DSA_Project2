"""
Huffman Coding

There are two phases to Huffman encoding:

1. building the Huffman tree (a binary tree)
2. generating the encoded data

"""
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


def print_nodes(node, coding_val=''):
    """Recursive function to print the leaf nodes of a huffman tree

    Args:
        node (HuffmanNode): the current HuffmanNode we are processing.
        coding_val (str): the huffman code so far.
    """
    # huffman code for current node
    # - this gets built up as we traverse the tree.
    huffman_code = coding_val + node.coding_val

    # if node is not a leaf node then traverse the left and right nodes
    if node.left:
        print_nodes(node.left, huffman_code)
    if node.right:
        print_nodes(node.right, huffman_code)

    # if node is a leaf node then display it's huffman code
    if node.is_leaf_node():
        print(f"{node.key} = {huffman_code}")


def create_huffman_tree(message):
    """Calculates a huffman tree for the input message

    Args:
        message (str): the message to create the huffman tree from
    Returns:
        root_node (HuffmanNode): root node of the huffman tree
    """
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


def main():
    huffman_tree = create_huffman_tree('AAAAAAABBBCCCCCCCDDEEEEEE')
    # print the leaf nodes of the tree, generating the encoding for each character as we do this
    print_nodes(huffman_tree)
    # D	= 000
    # B = 001
    # E = 01
    # A = 10
    # C = 11


if __name__ == '__main__':
    main()
